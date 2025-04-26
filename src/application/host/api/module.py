from dependency_injector.containers import DeclarativeContainer
from fastapi import FastAPI

from src.application.services.todo_lists.todo_list_appservice import (
    TodoListAppService,
)


class HttpApiHostModule:
    @staticmethod
    def OnApplicationInitialization(
        app: FastAPI, services: DeclarativeContainer
    ):
        app.include_router(
            TodoListAppService,
            prefix="/todo",
            tags=["TodoList"],
        )
