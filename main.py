from src.application.host.app import app
from src.application.host.config import settings

if __name__ == "__main__":
    from uvicorn import run as uvicorn_run

    uvicorn_run(
        app,
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.ENVIRONMENT == "development",
    )
