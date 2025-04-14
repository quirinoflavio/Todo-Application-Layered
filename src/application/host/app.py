from fastapi import FastAPI

from src.application.host.containers.container import AppContainer
from src.application.host.module import HttpHostModule

app = FastAPI()
container = AppContainer()

HttpHostModule.OnApplicationInitialization(app, container)
