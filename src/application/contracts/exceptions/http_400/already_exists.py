from typing import Generic, TypeVar, Type, Optional
from fastapi import HTTPException, status

TResource = TypeVar("TResource")


class AlreadyExistsException(HTTPException, Generic[TResource]):
    def __init__(
        self,
        resource_type: Type[TResource],
        status_code: int = status.HTTP_400_BAD_REQUEST,
        additional_detail: Optional[str] = None,
    ):
        """
        Exception raised when an resource already exists.

        Args:
            resource_type (Type[TResource]): The type of the resource that already exists.
            status_code (int): HTTP status code for the exception. Defaults to 409 (Conflict).
            additional_detail (Optional[str]): Additional context or information to include in the error message.
        """
        if hasattr(resource_type, "__name__"):
            resource_name = resource_type.__name__
        elif hasattr(resource_type, "name"):
            resource_name = resource_type.name
        else:
            raise ValueError(
                "Invalid resource_type: must be a class or type with a __name__ attribute."
            )

        detail = f"{resource_name} already exists."
        if additional_detail:
            detail += f" {additional_detail}"

        super().__init__(status_code=status_code, detail=detail)
