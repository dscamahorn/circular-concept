import anthropic as anthropic_sdk
import config


def _build_user_message(answers: dict, n_concepts: int, rag_context: str) -> str:
    return f"""**Question 1: What does the organization make or do?**
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


def call_anthropic(answers: dict, n_concepts: int, system_prompt: str, rag_context: str) -> str:
    user_message = _build_user_message(answers, n_concepts, rag_context)
    client = anthropic_sdk.Anthropic(api_key=config.ANTHROPIC_API_KEY)
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8192,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )
    return response.content[0].text


def stream_anthropic(answers: dict, n_concepts: int, system_prompt: str, rag_context: str):
    """Generator that yields raw text chunks from the Anthropic streaming API."""
    user_message = _build_user_message(answers, n_concepts, rag_context)
    client = anthropic_sdk.Anthropic(api_key=config.ANTHROPIC_API_KEY)
    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=8192,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    ) as stream:
        for text in stream.text_stream:
            yield text