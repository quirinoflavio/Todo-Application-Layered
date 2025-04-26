from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column

from ...core.entities.base import Base
from ...core.utils.conventions import NamingConvention


class EntityModel(Base):
    __abstract__ = True

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if "__tablename__" not in cls.__dict__:
            cls.__tablename__ = NamingConvention.camel_to_snake(cls.__name__)
