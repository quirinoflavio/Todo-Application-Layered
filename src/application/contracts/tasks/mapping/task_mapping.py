from src.application.contracts.tasks.dtos.task_create_dto import TaskCreateDto
from src.application.contracts.tasks.dtos.task_dto import TaskDto
from src.application.contracts.tasks.dtos.task_update_dto import TaskUpdateDto
from src.core.mapper.object_mapper import ObjectMapper
from src.domain.tasks.task import Task
from src.infrastructure.sqlalchemy.models.tasks.task_model import TaskModel


class TaskMapping:
    @classmethod
    def register(cls):
        ObjectMapper.create_map(TaskCreateDto, Task)
        ObjectMapper.create_map(TaskUpdateDto, Task)
        ObjectMapper.create_map(Task, TaskDto)
        ObjectMapper.create_map(TaskModel, TaskDto)
