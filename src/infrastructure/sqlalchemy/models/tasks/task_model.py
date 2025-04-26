from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...core.entities.audited_entity_model import AuditedEntityModel

if TYPE_CHECKING:
    from ..todo_lists.todo_list_model import TodoListModel


class TaskModel(AuditedEntityModel):
    title: Mapped[str]
    description: Mapped[str | None]
    is_completed: Mapped[bool] = mapped_column(default=False)
    due_date: Mapped[datetime | None]

    todo_list_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("todo_list.id"), nullable=False
    )

    todo_list: Mapped["TodoListModel"] = relationship(
        "TodoListModel", back_populates="tasks"
    )

    def __repr__(self) -> str:
        return f"<TaskModel {self.title}, Completed={self.is_completed}>"
