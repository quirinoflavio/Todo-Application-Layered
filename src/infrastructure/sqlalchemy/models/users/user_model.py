from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.sqlalchemy.core.entities.audited_entity_model import (
    AuditedEntityModel,
)

if TYPE_CHECKING:
    from ..todo_lists.todo_list_model import TodoListModel


class UserModel(AuditedEntityModel):
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
    is_verified: Mapped[bool] = mapped_column(default=False)

    todo_lists: Mapped[list["TodoListModel"]] = relationship(
        "TodoListModel", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<UserModel {self.email}>"
