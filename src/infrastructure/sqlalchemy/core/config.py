from pydantic_settings import BaseSettings


class Config(BaseSettings):

    DB_URL: str = "sqlite:///./test.db"
    DB_VERBOSE: bool = False


settings = Config()
