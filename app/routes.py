import anthropic as anthropic_sdk
from flask import redirect, render_template, request, session, url_for, jsonify

import config
from app.parser import _parse_llm_output


def _load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


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
        session["answers"] = answers

        n_concepts = int(request.form.get("n_concepts", 3))
        n_concepts = max(1, min(8, n_concepts))

        system_prompt = _load_file(config.PROMPT_FILE)
        rag_cpr = _load_file(config.CPR_RAG)
        rag_fwu = _load_file(config.FWU_RAG)

        user_message = f"""**Question 1: What does the organization make or do?**
{answers["q1"]}

**Question 2: Where does waste, inefficiency, or end-of-life live in their value chain?**
{answers["q2"]}

**Question 3: What pressure is driving the need to change?**
{answers["q3"]}

**Question 4: What circular territory have they already explored?**
{answers["q4"]}

**Question 5: What does a successful outcome look like for them?**
{answers["q5"]}

---

**Number of concepts to generate:** {n_concepts}

**RAG context:**

[Consumer Packaging Reuse]
{rag_cpr}

[Food Waste and Upcycling]
{rag_fwu}
"""

        try:
            client = anthropic_sdk.Anthropic(api_key=config.ANTHROPIC_API_KEY)
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=8192,
                system=system_prompt,
                messages=[{"role": "user", "content": user_message}],
            )
            concepts_text = response.content[0].text
        except Exception as e:
            return render_template("error.html", message=str(e)), 500

        profile_analysis, themes, concepts = _parse_llm_output(concepts_text)
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
            "gemini_key_set": bool(config.GEMINI_API_KEY),
        })