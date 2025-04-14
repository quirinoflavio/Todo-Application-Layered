from dependency_injector.containers import DeclarativeContainer
from fastapi import FastAPI

from src.application.host.middlewares.exception_handlers.business_exception_handler import (
    BusinessExceptionHandler,
)
from src.core.exceptions.business_exception import BusinessException


class ExceptionHandlerMiddleware:
    @staticmethod
    def OnApplicationInitialization(
        app: FastAPI, services: DeclarativeContainer
    ):
        app.add_exception_handler(
            BusinessException, BusinessExceptionHandler.handle
        )
