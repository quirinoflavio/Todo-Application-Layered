from dependency_injector.containers import DeclarativeContainer
from fastapi import FastAPI

from application.contracts.tasks.mapping.task_mapping import TaskMapping
from application.contracts.todo_lists.mapping.todo_list_mapping import (
    TodoListMapping,
)


class ObjectMapperModule:
    @staticmethod
    def OnApplicationInitialization(
        app: FastAPI, services: DeclarativeContainer
    ):
        TodoListMapping.register()
        TaskMapping.register()
