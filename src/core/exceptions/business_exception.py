from src.core.exceptions.business_error_enum import BusinessErrorEnum


class BusinessException(Exception):
    def __init__(self, error: BusinessErrorEnum, *args, **kwargs):
        resource = kwargs.get("resource", None)

        if resource:
            self.message = (
                f"{resource.__name__}: {error.message}"
                if hasattr(resource, "__name__")
                else f"{str(resource)}: {error.message}"
            )
        else:
            self.message = error.message

        self.code = error.code
        self.error = error
        self.resource = resource

        super().__init__(self.message, *args)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.code} - {self.message}"
