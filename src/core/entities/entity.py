import uuid
from typing import Any, TypeVar

from pydantic import BaseModel, Field

EntityType = TypeVar("EntityType", bound="Entity")


class Identity(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)


class Entity(Identity):
    @classmethod
    def empty(cls):
        # Initialize fields with default or None
        field_values = {
            field_name: field.default if field.default is not None else None
            for field_name, field in cls.model_fields.items()
        }
        return cls(**field_values)

