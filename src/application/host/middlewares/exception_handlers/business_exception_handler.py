from typing import Dict, Type

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

from src.application.contracts.exceptions.http_400.already_exists import (
    AlreadyExistsException,
)
from src.application.contracts.exceptions.http_400.not_found import (
    NotFoundException,
)
from src.core.exceptions.business_error_enum import BusinessErrorEnum
from src.core.exceptions.business_exception import BusinessException


class BusinessExceptionHandler:
    """Handles business exceptions and maps them to appropriate HTTP responses."""

    ERROR_MAPPING: Dict[BusinessErrorEnum, Type[HTTPException]] = {
        BusinessErrorEnum.AlreadyExists: AlreadyExistsException,
        BusinessErrorEnum.NotFound: NotFoundException,
        # Future error mappings can be added here
    }

    @staticmethod
    async def handle(request: Request, exc: BusinessException) -> JSONResponse:
        """Handles BusinessException and returns an appropriate JSON response."""
        exception_class = BusinessExceptionHandler.ERROR_MAPPING.get(exc.error)

        if not exception_class:
            # Default to 500 Internal Server Error for unknown exceptions
            return JSONResponse(
                status_code=500,
                content={"detail": "Unexpected error occurred."},
            )

        exception = exception_class(
            resource_type=exc.resource, additional_detail=exc.message
        )

        return JSONResponse(
            status_code=exception.status_code, content=exception.__dict__
        )
