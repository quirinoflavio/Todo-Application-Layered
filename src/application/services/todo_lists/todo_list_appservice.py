from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.contracts.todo_lists.dtos.todo_list_create_dto import (
    TodoListCreateDto,
)
from src.application.contracts.todo_lists.dtos.todo_list_dto import TodoListDto
from src.application.host.containers.container import AppContainer
from src.core.mapper.object_mapper import ObjectMapper
from src.domain.todo_lists.todo_list import TodoList
from src.domain.todo_lists.todo_list_manager import TodoListManager
from src.infrastructure.sqlalchemy.core.database import DatabaseProvider
from src.infrastructure.sqlalchemy.repositories.todo_lists.todo_list_repository import (
    TodoListRepository,
)

TodoListAppService = APIRouter()


@TodoListAppService.post("/", status_code=status.HTTP_201_CREATED)
@inject
async def create(
    create_dto: TodoListCreateDto,
    todo_list_manager: TodoListManager = Depends(
        Provide[AppContainer.managers.todo_list_manager]
    ),
    todo_list_repository: TodoListRepository = Depends(
        Provide[AppContainer.repositories.todo_list_repository]
    ),
    db_session: AsyncSession = Depends(DatabaseProvider.get_db),
) -> TodoListDto:
    async with db_session.begin():
        todo_list: TodoList = ObjectMapper.map(create_dto, TodoList)

        await todo_list_repository.insert(todo_list, db_session)

    todo_list_dto = ObjectMapper.map(todo_list, TodoListDto)

    return todo_list_dto
