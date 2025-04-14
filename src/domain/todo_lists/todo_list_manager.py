from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from domain.todo_lists.todo_list import TodoList
from infrastructure.sqlalchemy.repositories.todo_lists.todo_list_repository import (
    TodoListRepository,
)

# TODO: Descobrir como isolar o dominio da infraestrutura.
#       ITodoListRepository funciona?


class TodoListManager:
    def __init__(
        self,
        todo_list_repository: TodoListRepository,
    ):
        self.todo_list_repository = todo_list_repository

    async def restore(
        self,
        todo_list_id: UUID,
        db_session: AsyncSession = None,
    ) -> TodoList:
        todo_list: TodoList = await self.todo_list_repository.get(
            todo_list_id, db_session=db_session
        )

        for task in todo_list.tasks:
            task.is_completed = False

        await self.todo_list_repository.update(
            todo_list, db_session=db_session
        )

        return todo_list
