from application.contracts.todo_lists.dtos.todo_list_create_dto import (
    TodoListCreateDto,
)
from application.contracts.todo_lists.dtos.todo_list_dto import TodoListDto
from application.contracts.todo_lists.dtos.todo_list_update_dto import (
    TodoListUpdateDto,
)
from core.mapper.object_mapper import ObjectMapper
from domain.todo_lists.todo_list import TodoList
from infrastructure.sqlalchemy.models.todo_lists.todo_list_model import (
    TodoListModel,
)


class TodoListMapping:
    @classmethod
    def register(cls):
        ObjectMapper.create_map(TodoListCreateDto, TodoList)
        ObjectMapper.create_map(TodoListUpdateDto, TodoList)
        ObjectMapper.create_map(TodoList, TodoListDto)
        ObjectMapper.create_map(TodoListModel, TodoListDto)
