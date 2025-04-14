from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...core.entities.entity_model import EntityModel

if TYPE_CHECKING:
    from ..tasks.task_model import TaskModel
    from ..users.user_model import UserModel


class TodoListModel(EntityModel):
    title: Mapped[str]
    description: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("user.id"), nullable=False
    )
    user: Mapped["UserModel"] = relationship(
        "UserModel", back_populates="todo_lists"
    )

    tasks: Mapped[list["TaskModel"]] = relationship(
        "TaskModel", back_populates="todo_list", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<TodoListModel {self.title}>"
