from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    GOOGLE_API_KEY: str = "test"
    app_name: str = "ComicCraftAI"
    APP_NAME: str = "ComicCraftAI"
    
    # Ithu than main fix - str ku pathila Path
    output_dir: Path = Path("output")
    OUTPUT_DIR: Path = Path("output")
    static_dir: Path = Path("static")
    upload_dir: Path = Path("uploads")
    
    image_provider: str = "huggingface"
    use_local_diffusers: bool = False
    local_diffusion_model: str = "runwayml/stable-diffusion-v1-5"

    model_config = SettingsConfigDict(env_file=".env", extra="allow")

def get_settings():
    return Settings()

settings = Settings()
settings.output_dir.mkdir(parents=True, exist_ok=True)