from pydantic_settings import BaseSettings


class Config(BaseSettings):

    DB_URL: str = "sqlite:///./test.db"
    DB_VERBOSE: bool = False


settings = Config()

# # Database Configuration
# DB_USERNAME = os.getenv("DB_USERNAME", "cepostgres")
# DB_PASSWORD = os.getenv("DB_PASSWORD", "cepostgres")
# DB_HOST = os.getenv("DB_HOST", "localhost")
# DB_PORT = int(os.getenv("DB_PORT", "5432"))
# DB_NAME = os.getenv("DB_NAME", "comply-local1")
# LOG_SQL = os.getenv("LOGSQL", "true").lower() == "true"
# DROP_ALL = os.getenv("DROP_ALL", "true").lower() == "true"

# # Construct the database URL
# DATABASE_URL = URL.create(
#     drivername="postgresql+asyncpg",
#     username=DB_USERNAME,
#     password=DB_PASSWORD,
#     host=DB_HOST,
#     port=DB_PORT,
#     database=DB_NAME,
# )
