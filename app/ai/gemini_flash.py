from app.config import get_settings
from app.schemas import (
    OutlineResponse,
    PromptRequest,
)

from app.services.demo_data import demo_outline


def generate_outline(
    request: PromptRequest
):

    settings = get_settings()

    # Demo mode.
    if settings.demo_enabled:
        return demo_outline(request)

    if not settings.gemini_api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not configured."
        )

    from google import genai
    from google.genai import types

    client = genai.Client(
        api_key=settings.gemini_api_key
    )

    prompt = f"""
Create exactly {settings.panels} connected comic panels.

User story idea:
{request.story_prompt}

Main character:
{request.character_name}

Setting:
{request.setting}

Tone:
{request.tone}

Art style:
{request.art_style}

Requirements:

1. Create exactly five panels.
2. Keep the same main character throughout.
3. Maintain story continuity.
4. Give every panel a title.
5. Give every panel a concise scene description.
6. Create a detailed image-generation prompt.
7. Image prompts must describe visual content.
8. Do not include lettering.
9. Do not include speech bubbles.
10. Do not include logos.
11. Do not include watermarks.
"""

    response = client.models.generate_content(
        model=settings.gemini_flash_model,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=OutlineResponse,
            temperature=0.9,
        ),
    )

    if not response.text:
        raise RuntimeError(
            "Gemini returned an empty response."
        )

    parsed = OutlineResponse.model_validate_json(
        response.text
    )

    if len(parsed.panels) != settings.panels:
        raise ValueError(
            f"Gemini returned "
            f"{len(parsed.panels)} panels; "
            f"expected {settings.panels}."
        )

    return parsed.panels