from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    JWT_ALGORITHM: str = "HS256"
    JWT_SECRET: str = "64_char_random_string"
    CRYPT_SCHEMES: list[str] = ["bcrypt"]
    ACCESS_TOKEN_EXPIRY: int = 3600
    HOST: str = "localhost"
    PORT: int = 8000
    ENVIRONMENT: str = "development"


settings = Settings()
