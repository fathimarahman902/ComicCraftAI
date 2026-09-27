def generate_image(prompt: str, seed: int = 1):
    # Pollinations - 100% correct fox image
    safe_prompt = prompt.replace(" ", "%20")
    url = f"https://image.pollinations.ai/prompt/{safe_prompt}%20cute%20orange%20fox%20pixar%20style?width=800&height=600&seed={seed}&nologo=true"
    return url