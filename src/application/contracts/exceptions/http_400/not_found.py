from typing import Generic, Optional, Type, TypeVar
from fastapi import HTTPException, status

TResource = TypeVar("TResource")
TResourceId = TypeVar("TResourceId")


class NotFoundException(HTTPException, Generic[TResource, TResourceId]):
    def __init__(
        self,
        resource_type: Type[TResource],
        resource_id: Type[TResourceId] = None,
        status_code: int = status.HTTP_404_NOT_FOUND,
        additional_detail: Optional[str] = None,
    ):
        """
        Exception raised when the resource is not found.

        Args:
            resource_type (Type[TResource]): The type of the resource that was not found.
            status_code (int): HTTP status code for the exception. Defaults to 409 (Conflict).
            additional_detail (Optional[str]): Additional context or information to include in the error message.
        """
        if not resource_type or not hasattr(resource_type, "__name__"):
            raise ValueError(
                "Invalid resource_type: must be a class or type with a __name__ attribute."
            )

        detail = f"{resource_type.__name__} was not found."
        if resource_id:
            detail += f" Id: {str(resource_id)}"
        if additional_detail:
            detail += f" {additional_detail}"

        super().__init__(status_code=status_code, detail=detail)
