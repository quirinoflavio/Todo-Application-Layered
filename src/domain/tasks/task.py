from datetime import datetime
from uuid import UUID

from core.entities.entity import Entity


class Task(Entity):
    id: UUID
    todo_list_id: UUID
    title: str
    description: str | None
    is_completed: bool
    due_date: datetime | None
    created_at: datetime
    