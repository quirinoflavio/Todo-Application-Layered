from datetime import datetime, timezone
from uuid import uuid4

from pydantic import Field

from domain.tasks.task import Task
from src.core.entities.aggregate_root import AggregateRoot


class TodoList(AggregateRoot):
    tasks: list[Task] = Field(default_factory=list)

    def add_task(
        self,
        title: str,
        description: str | None = None,
        due_date: datetime | None = None,
    ):
        task = Task(
            id=uuid4(),
            todo_list_id=self.id,
            title=title,
            description=description,
            is_completed=False,
            due_date=due_date,
            created_at=datetime.now(timezone.utc),
        )
        self.tasks.append(task)
