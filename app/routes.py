import base64
import json
import re
import uuid

from flask import Response, redirect, render_template, request, session, stream_with_context, url_for, jsonify

import config
from app.llm import call_anthropic, stream_anthropic
from app.image_gen import build_image_prompt, call_gemini_image
from app.parser import _parse_llm_output
from app.rag import load_rag_context

# Server-side cache for streamed concept results, keyed by per-request UUID.
# Populated by /generate-stream, consumed once by /concepts.
_concept_cache: dict = {}


def register_routes(app):

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/survey")
    def survey():
        existing = session.get("answers", {})
        return render_template("survey.html", existing=existing)

    @app.route("/submit", methods=["POST"])
    def submit():
        answers = {
            "q1": request.form.get("q1", "").strip(),
            "q2": request.form.get("q2", "").strip(),
            "q3": request.form.get("q3", "").strip(),
            "q4": request.form.get("q4", "").strip(),
            "q5": request.form.get("q5", "").strip(),
        }
        session["answers"] = answers
        return render_template("review.html", answers=answers)

    @app.route("/review")
    def review():
        answers = session.get("answers")
        if not answers:
            return redirect(url_for("index"))
        return render_template("review.html", answers=answers)

    @app.route("/generate", methods=["POST"])
    def generate():
        answers = {
            "q1": request.form.get("q1", "").strip(),
            "q2": request.form.get("q2", "").strip(),
            "q3": request.form.get("q3", "").strip(),
            "q4": request.form.get("q4", "").strip(),
            "q5": request.form.get("q5", "").strip(),
        }
        n_concepts = max(1, min(8, int(request.form.get("n_concepts", 3))))

        try:
            system_prompt = config.load_file(config.PROMPT_FILE)
            rag_context   = load_rag_context()
            raw           = call_anthropic(answers, n_concepts, system_prompt, rag_context)
        except Exception as e:
            return render_template("error.html", message=str(e)), 500

        profile_analysis, themes, concepts = _parse_llm_output(raw)
        return render_template(
            "concepts.html",
            profile_analysis=profile_analysis,
            themes=themes,
            concepts=concepts,
            n_concepts=n_concepts,
        )

    @app.route("/generate-stream", methods=["POST"])
    def generate_stream():
        answers    = {f"q{i}": request.form.get(f"q{i}", "").strip() for i in range(1, 6)}
        n_concepts = max(1, min(8, int(request.form.get("n_concepts", 3))))
        session["answers"] = answers

        stream_key = str(uuid.uuid4())
        session["stream_key"] = stream_key

        def sse(payload: dict) -> str:
            return f"data: {json.dumps(payload)}\n\n"

        def generate():
            try:
                system_prompt = config.load_file(config.PROMPT_FILE)
                rag_context   = load_rag_context()
            except Exception as e:
                yield sse({"type": "error", "message": str(e)})
                return

            accumulated          = ""
            concept_starts_seen  = 0
            concept_ends_seen    = 0

            try:
                for chunk in stream_anthropic(answers, n_concepts, system_prompt, rag_context):
                    accumulated += chunk

                    new_starts = len(re.findall(r'<concept number="\d+">', accumulated))
                    while concept_starts_seen < new_starts:
                        concept_starts_seen += 1
                        yield sse({"type": "concept_start", "number": concept_starts_seen})

                    new_ends = accumulated.count("</concept>")
                    while concept_ends_seen < new_ends:
                        concept_ends_seen += 1
                        yield sse({"type": "concept_end", "number": concept_ends_seen})

            except Exception as e:
                yield sse({"type": "error", "message": str(e)})
                return

            try:
                profile_analysis, themes, concepts = _parse_llm_output(accumulated)
                _concept_cache[stream_key] = {
                    "profile_analysis": profile_analysis,
                    "themes":           themes,
                    "concepts":         concepts,
                    "n_concepts":       n_concepts,
                }
                yield sse({"type": "done"})
            except Exception as e:
                yield sse({"type": "error", "message": str(e)})

        return Response(
            stream_with_context(generate()),
            mimetype="text/event-stream",
            headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
        )

    @app.route("/concepts")
    def concepts():
        stream_key = session.get("stream_key")
        if not stream_key or stream_key not in _concept_cache:
            return redirect(url_for("index"))
        data = _concept_cache.pop(stream_key)
        return render_template("concepts.html", **data)

    @app.route("/visualize", methods=["POST"])
    def visualize():
        data         = request.get_json(silent=True) or {}
        image_fields = data.get("image_fields") or {}
        if not image_fields:
            return jsonify({"error": "No image fields provided"}), 400

        prompt = build_image_prompt(image_fields)
        if prompt is None:
            return jsonify({"error": "Could not parse prototype sentence"}), 422

        try:
            png_bytes = call_gemini_image(prompt)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

        b64 = base64.b64encode(png_bytes).decode("utf-8")
        return jsonify({"image": f"data:image/png;base64,{b64}"})

    @app.route("/start-over")
    def start_over():
        session.pop("answers", None)
        return redirect(url_for("index"))

    @app.route("/ping")
    def ping():
        return "pong — server is alive"

    @app.route("/health")
    def health():
        return jsonify({
            "status": "ok",
            "anthropic_key_set": bool(config.ANTHROPIC_API_KEY),
            "gemini_key_set":    bool(config.GEMINI_API_KEY),
        })