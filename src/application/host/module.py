from dependency_injector.containers import DeclarativeContainer
from fastapi import FastAPI

from src.application.host.api.module import HttpApiHostModule
from src.application.host.api.object_mapper.module import ObjectMapperModule
from src.application.host.containers.module import DependecyInjectionModule
from src.application.host.middlewares.module import ExceptionHandlerMiddleware
from src.infrastructure.sqlalchemy.mapping.orm_mapping import OrmMappingModule


class HttpHostModule:
    def OnApplicationInitialization(
        app: FastAPI, services: DeclarativeContainer
    ):
        DependecyInjectionModule.OnApplicationInitialization(app, services)

        ObjectMapperModule.OnApplicationInitialization(app, services)

        HttpApiHostModule.OnApplicationInitialization(app, services)

        OrmMappingModule.OnApplicationInitialization(app, services)

        ExceptionHandlerMiddleware.OnApplicationInitialization(app, services)
