import base64

from google import genai
from google.genai import types

import config


def call_gemini_image(prompt: str) -> bytes:
    """
    Calls the Gemini image generation model and returns raw PNG bytes.
    Raises on API error or if no image part is found in the response.
    """
    client = genai.Client(api_key=config.GEMINI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
        ),
    )
    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            return part.inline_data.data
    raise ValueError("Gemini response contained no image part")


def build_image_prompt(image_fields: dict) -> str | None:
    """
    Loads image_prompt.md, strips the developer-only Integration Mapping section,
    substitutes the pre-parsed image fields, and returns the final prompt string.
    Returns None if any required field is missing.
    """
    required = ("loop_name_caps", "narrative_1", "narrative_2", "narrative_3", "narrative_4")
    if not all(image_fields.get(k) for k in required):
        return None

    raw      = config.load_file(config.IMAGE_PROMPT_FILE)
    template = raw.split("### Integration Mapping")[0].rstrip()

    return (
        template
        .replace("[LOOP_NAME_CAPS]",   image_fields["loop_name_caps"])
        .replace("[NARRATIVE_1_TEXT]", image_fields["narrative_1"])
        .replace("[NARRATIVE_2_TEXT]", image_fields["narrative_2"])
        .replace("[NARRATIVE_3_TEXT]", image_fields["narrative_3"])
        .replace("[NARRATIVE_4_TEXT]", image_fields["narrative_4"])
    )