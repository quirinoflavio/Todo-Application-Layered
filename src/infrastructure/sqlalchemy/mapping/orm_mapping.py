from sqlalchemy.orm import registry

from src.domain.tasks.task import Task
from src.domain.todo_lists.todo_list import TodoList
from src.domain.users.user import User
from src.infrastructure.sqlalchemy.models.tasks.task_model import TaskModel
from src.infrastructure.sqlalchemy.models.todo_lists.todo_list_model import (
    TodoListModel,
)
from src.infrastructure.sqlalchemy.models.users.user_model import UserModel


class OrmMappingModule:
    @staticmethod
    def OnApplicationInitialization(app, services):
        """
        initialize orm mappings
        """
        mapper_registry = registry()

        mapper_registry.map_imperatively(TodoList, TodoListModel.__table__)
        mapper_registry.map_imperatively(Task, TaskModel.__table__)
        mapper_registry.map_imperatively(User, UserModel.__table__)
