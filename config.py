import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).parent


def load_file(path) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
GEMINI_API_KEY    = os.environ.get("GEMINI_API_KEY")
SECRET_KEY        = os.environ.get("SECRET_KEY", "dev-change-this-in-production")

PROMPT_FILE = ROOT / "prompts" / "system_prompt.md"
CPR_RAG     = ROOT / "knowledge" / "RAG_consumer_packaging_reuse.xml"
FWU_RAG     = ROOT / "knowledge" / "RAG_food_waste_upcycling.xml"