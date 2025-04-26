from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    DB_URL: str = "sqlite:///./test.db"
    DB_VERBOSE: bool = False

    model_config = SettingsConfigDict(env_file=".env")


settings = Config()
