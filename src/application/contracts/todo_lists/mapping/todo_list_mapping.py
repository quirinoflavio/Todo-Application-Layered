from src.application.contracts.todo_lists.dtos.todo_list_create_dto import (
    TodoListCreateDto,
)
from src.application.contracts.todo_lists.dtos.todo_list_dto import TodoListDto
from src.application.contracts.todo_lists.dtos.todo_list_update_dto import (
    TodoListUpdateDto,
)
from src.core.mapper.object_mapper import ObjectMapper
from src.domain.todo_lists.todo_list import TodoList
from src.infrastructure.sqlalchemy.models.todo_lists.todo_list_model import (
    TodoListModel,
)


class TodoListMapping:
    @classmethod
    def register(cls):
        ObjectMapper.create_map(TodoListCreateDto, TodoList)
        ObjectMapper.create_map(TodoListUpdateDto, TodoList)
        ObjectMapper.create_map(TodoList, TodoListDto)
        ObjectMapper.create_map(TodoListModel, TodoListDto)
