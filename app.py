import os
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

load_dotenv()

app = Flask(__name__)

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")


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
    return render_template("result.html", answers=answers)


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
