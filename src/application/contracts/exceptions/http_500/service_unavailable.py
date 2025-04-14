from typing import Optional, Type, TypeVar

from fastapi import HTTPException, status

TResource = TypeVar("TResource")


class ServiceUnavailableException(HTTPException):
    def __init__(
        self,
        service: Type[TResource],
        status_code: int = status.HTTP_503_SERVICE_UNAVAILABLE,
        additional_detail: Optional[str] = None,
    ):
        """
        Exception raised when a service is unavailable.

        Args:
            service_name (str): The name of the service that is unavailable.
            status_code (int): HTTP status code for the exception. Defaults to 503 (Service Unavailable).
            additional_detail (Optional[str]): Additional context or information to include in the error message.
        """
        if hasattr(service, "__name__"):
            service_name = service.__name__
        elif hasattr(service, "name"):
            service_name = service.name
        else:
            raise ValueError(
                "Invalid service: must be a class or type with a __name__ attribute."
            )

        detail = f"Service {service_name} is currently unavailable."
        if additional_detail:
            detail += f" {additional_detail}"

        super().__init__(status_code=status_code, detail=detail)
