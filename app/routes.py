from flask import redirect, render_template, request, session, url_for, jsonify

import config
from app.llm import call_anthropic
from app.parser import _parse_llm_output
from app.rag import load_rag_context


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