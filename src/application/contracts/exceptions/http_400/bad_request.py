from typing import Generic, TypeVar, Type, Optional
from fastapi import HTTPException, status

TResource = TypeVar("TResource")


class BadRequestException(HTTPException, Generic[TResource]):
    def __init__(
        self,
        resource_type: Type[TResource] = None,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        additional_detail: Optional[str] = "",
    ):
        """
        Exception raised for a bad request.

        Args:
            resource_type (Type[TResource]): The type of the resource related to the bad request.
            status_code (int): HTTP status code for the exception. Defaults to 400 (Bad Request).
            additional_detail (Optional[str]): Additional context or information to include in the error message.
        """
        if resource_type is None:
            detail = "."
        elif hasattr(resource_type, "__name__"):
            detail = f" for {resource_type.__name__}."
        elif hasattr(resource_type, "name"):
            detail = f" for {resource_type.name}."
        else:
            raise ValueError(
                "Invalid resource_type: must be a class or type with a __name__ attribute."
            )

        error_message = "Bad Request" + detail + additional_detail

        super().__init__(status_code=status_code, detail=error_message)
