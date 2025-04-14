from typing import Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from infrastructure.sqlalchemy.models.todo_lists.todo_list_model import (
    TodoListModel,
)


class TodoListRepository:

    def __init__(self):
        """
        Initialize the TodoListRepository.

        """

    async def insert(
        self,
        todo_list: TodoListModel,
        db_session: AsyncSession = None,
    ):
        """
        Inserts a todo list into the database.

        Args:
            todo_list (TodoListModel): The todo list to insert.
            db_session (AsyncSession): The database session to use.
        """
        db_session.add(todo_list)
        await db_session.flush()

    async def insert_many(
        self,
        todo_lists: list[TodoListModel],
        db_session: AsyncSession = None,
    ):
        """
        Inserts a set of todo lists into the database.

        Args:
            todo_lists (list[TodoListModel]): The set of todo lists to insert.
            db_session (AsyncSession): The database session to use.
        """
        db_session.add_all(todo_lists)
        await db_session.flush()

    async def get(
        self,
        id: UUID,
        db_session: AsyncSession = None,
        include_details=False,
    ) -> TodoListModel:
        """
        Finds a todo list by its ID.

        Args:
            id (UUID): The ID of the todo list.
            db_session (AsyncSession): The database session to use.

        Returns:
            TodoListModel: The todo list with the specified ID.
        """
        stmt = select(TodoListModel).where(TodoListModel.id == id)

        if include_details:
            stmt = stmt.options(selectinload(TodoListModel.tasks))

        result = await db_session.execute(stmt)
        todo_list = result.scalars().first()
        return todo_list

    async def update(
        self,
        todo_list: TodoListModel,
        db_session: AsyncSession = None,
    ) -> Optional[TodoListModel]:
        """
        Updates a todo list by its ID.

        Args:
            todo_list (TodoListModel): The data to update the todo list with.
            db_session (AsyncSession): The database session to use.

        Returns:
            Optional[TodoListModel]: The updated todo list.
        """
        db_session.add(todo_list)
        await db_session.flush()

    async def delete(self, id: UUID, db_session: AsyncSession = None):
        """
        Deletes a todo list by its ID.

        Args:
            id (UUID): The ID of the todo list to delete.
            db_session (AsyncSession): The database session to use.
        """
        todo_list = await self.get(id, db_session)
        if todo_list:
            await db_session.delete(todo_list)
            await db_session.flush()

    async def get_all(
        self, db_session: AsyncSession = None
    ) -> list[TodoListModel]:
        """
        Retrieves all todo lists from the database.

        Args:
            db_session (AsyncSession): The database session to use.

        Returns:
            List[TodoListModel]: A list of all todo lists .
        """
        stmt = select(TodoListModel)
        result = await db_session.execute(stmt)
        todo_lists = result.scalars().all()
        return todo_lists
