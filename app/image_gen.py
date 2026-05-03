import base64
import re

from google import genai
from google.genai import types

import config


def parse_prototype(sentence: str) -> dict | None:
    """
    Parses a prototype sentence of the form:
      "[User action], and in return [user receives], while [actor] closes
       the [loop name] loop by [Z]."
    Returns a dict of image prompt variables, or None if the pattern doesn't match.
    """
    pattern = re.compile(
        r'^(.+?)\s+and in return\s+(.+?),?\s+while\s+(.+?)\s+closes\s+the\s+(.+?)\s+loop\s+by\s+(.+?)\.?\s*$',
        re.IGNORECASE | re.DOTALL,
    )
    m = pattern.match(sentence.strip())
    if not m:
        return None

    user_action   = m.group(1).strip()
    user_receives = m.group(2).strip()
    actor         = m.group(3).strip()
    loop_name     = m.group(4).strip()
    z             = m.group(5).strip()

    return {
        "loop_name_caps": loop_name.upper(),
        "narrative_1":    user_action,
        "narrative_2":    user_receives,
        "narrative_3":    f"{actor} closes the {loop_name} loop",
        "narrative_4":    z,
    }


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


def build_image_prompt(prototype: str) -> str | None:
    """
    Loads image_prompt.md and DESIGN.md, substitutes prototype variables,
    and returns the final prompt string. Returns None if parsing fails.
    """
    fields = parse_prototype(prototype)
    if fields is None:
        return None

    template = config.load_file(config.IMAGE_PROMPT_FILE)
    design   = config.load_file(config.DESIGN_FILE)

    prompt = (
        template
        .replace("[LOOP_NAME_CAPS]",   fields["loop_name_caps"])
        .replace("[NARRATIVE_1_TEXT]", fields["narrative_1"])
        .replace("[NARRATIVE_2_TEXT]", fields["narrative_2"])
        .replace("[NARRATIVE_3_TEXT]", fields["narrative_3"])
        .replace("[NARRATIVE_4_TEXT]", fields["narrative_4"])
    )

    return f"{prompt}\n\n---\n\n**DESIGN.md**\n\n{design}"