from dependency_injector.containers import DeclarativeContainer
from fastapi import FastAPI


class DependecyInjectionModule:
    @staticmethod
    def OnApplicationInitialization(
        app: FastAPI, services: DeclarativeContainer
    ):
        services.wire(modules=["src.application.services"])
        services.init_resources()
        app.services = services
