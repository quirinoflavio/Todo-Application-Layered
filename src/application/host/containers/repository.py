from dependency_injector import containers, providers

from src.infrastructure.sqlalchemy.core.database import DatabaseProvider
from src.infrastructure.sqlalchemy.repositories.todo_lists.todo_list_repository import (
    TodoListRepository,
)


class RepositoryContainer(containers.DeclarativeContainer):
    session_factory = providers.Factory(DatabaseProvider.get_db)

    todo_list_repository = providers.Factory(
        TodoListRepository,
    )
