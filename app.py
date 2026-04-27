import os
import anthropic as anthropic_sdk
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

load_dotenv()

app = Flask(__name__)

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

BASE_DIR = os.path.dirname(__file__)

def _load_file(path):
    with open(os.path.join(BASE_DIR, path), "r", encoding="utf-8") as f:
        return f.read()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/survey")
def survey():
    return render_template("survey.html")


@app.route("/submit", methods=["POST"])
def submit():
    answers = {
        "q1": request.form.get("q1", "").strip(),
        "q2": request.form.get("q2", "").strip(),
        "q3": request.form.get("q3", "").strip(),
        "q4": request.form.get("q4", "").strip(),
        "q5": request.form.get("q5", "").strip(),
    }
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
    n_concepts = int(request.form.get("n_concepts", 3))
    n_concepts = max(1, min(8, n_concepts))

    system_prompt = _load_file("instructions/PROMPT_PROTOTYPE.md")
    rag_context = _load_file("data/RAG_consumer_packaging_reuse.md")

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
{rag_context}
"""

    client = anthropic_sdk.Anthropic(api_key=ANTHROPIC_API_KEY)
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8192,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )

    concepts_text = response.content[0].text
    return render_template("concepts.html", concepts=concepts_text, n_concepts=n_concepts)


@app.route("/ping")
def ping():
    return "pong — server is alive"


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "anthropic_key_set": bool(ANTHROPIC_API_KEY),
        "gemini_key_set": bool(GEMINI_API_KEY),
    })


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", "false").lower() == "true")
