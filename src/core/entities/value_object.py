from typing import Any, TypeVar
from enum import EnumMeta
from pydantic import BaseModel, Field

from src.core.entities.exception import ValueObjectEnumError

ValueObjectType = TypeVar("ValueObjectType", bound="ValueObject")


class ValueObject(BaseModel):
    value: Any = Field(...)

    def __composite_values__(self):
        return (self.value,)

    @classmethod
    def from_value(cls, value: Any) -> ValueObjectType:
        if isinstance(cls, EnumMeta):
            for item in cls:
                if item.value == value:
                    return item
            raise ValueObjectEnumError

        return cls(value=value)

    @classmethod
    def empty(cls):
        # Initialize fields with default or None
        field_values = {
            field_name: field.default if field.default is not None else None
            for field_name, field in cls.model_fields.items()
        }
        return cls(**field_values)
