from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SECRET_KEY: str = "change-me-in-prod"
    DATABASE_URL: str = "sqlite:///./dev.db"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
