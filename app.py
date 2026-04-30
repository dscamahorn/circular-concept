import os
import re
import anthropic as anthropic_sdk
from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request, session, url_for

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-change-this-in-production")

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

BASE_DIR = os.path.dirname(__file__)

def _load_file(path):
    with open(os.path.join(BASE_DIR, path), "r", encoding="utf-8") as f:
        return f.read()


def _parse_llm_output(text):
    """Parse structured LLM output into profile analysis + list of concept dicts."""

    def extract(block, field):
        m = re.search(
            rf'\*\*{re.escape(field)}:\*\*\s*(.*?)(?=\n\*\*|\Z)',
            block, re.DOTALL
        )
        return m.group(1).strip() if m else ""

    pm = re.search(
        r'\*\*Profile\s+analysis:\*\*\s*(.*?)(?=\n+---|\n+###|\Z)',
        text, re.DOTALL | re.IGNORECASE
    )
    if pm:
        profile = pm.group(1).strip()
    else:
        # Fallback: capture everything before the first --- or ### heading
        profile = re.split(r'\n+---+\n+|\n+###', text, maxsplit=1)[0].strip()

    concepts = []
    themes = ""
    for section in re.split(r'\n+---+\n+', text):
        hm = re.search(r'###\s*Concept\s*(\d+):\s*(.+)', section)
        if not hm:
            # Sections with no concept header after the first are the closing summary
            if concepts:
                themes = section.strip()
            continue
        concepts.append({
            "number":     int(hm.group(1)),
            "title":      hm.group(2).strip(),
            "mechanic":   extract(section, "Circular mechanic"),
            "user":       extract(section, "Target user"),
            "value_chain":extract(section, "Value chain inefficiency addressed"),
            "pressure":   extract(section, "Pressure addressed"),
            "description":extract(section, "Concept description"),
            "prototype":  extract(section, "Prototype-readiness sentence"),
            "verdict":    extract(section, "Prototype-readiness verdict"),
            "alignment":  extract(section, "Outcome alignment"),
            "assumptions":extract(section, "Assumptions to test"),
        })

    # Strip any leading markdown heading line (## Profile analysis, **Profile analysis**, etc.)
    profile_lines = profile.splitlines()
    if profile_lines and re.match(r'^(#{1,3}|\*{1,2})\s*profile\s+analysis', profile_lines[0].strip(), re.IGNORECASE):
        profile = '\n'.join(profile_lines[1:]).strip()

    return profile, themes, sorted(concepts, key=lambda c: c["number"])


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
        return redirect(url_for("survey"))
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

    try:
        client = anthropic_sdk.Anthropic(api_key=ANTHROPIC_API_KEY)
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
        "anthropic_key_set": bool(ANTHROPIC_API_KEY),
        "gemini_key_set": bool(GEMINI_API_KEY),
    })


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", "false").lower() == "true")
