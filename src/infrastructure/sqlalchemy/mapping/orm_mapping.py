from sqlalchemy.orm import registry

from domain.tasks.task import Task
from domain.todo_lists.todo_list import TodoList
from domain.users.user import User
from infrastructure.sqlalchemy.models.tasks.task_model import TaskModel
from infrastructure.sqlalchemy.models.todo_lists.todo_list_model import (
    TodoListModel,
)
from infrastructure.sqlalchemy.models.users.user_model import UserModel


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
