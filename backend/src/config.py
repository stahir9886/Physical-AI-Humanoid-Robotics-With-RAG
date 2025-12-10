from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # API Configuration
    openai_api_key: Optional[str] = None
    qdrant_host: str = "localhost"
    qdrant_port: int = 6333
    neon_database_url: Optional[str] = None
    rate_limit_requests: int = 100
    rate_limit_window: int = 3600  # in seconds

    # Application Configuration
    environment: str = "development"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
        case_sensitive = False


# Create a global settings instance
settings = Settings()