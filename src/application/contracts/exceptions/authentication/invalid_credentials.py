from fastapi import HTTPException, status


class InvalidCredentials(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_403_FORBIDDEN,
        detail: str = "Invalid Email or Password.",
    ):
        super().__init__(status_code=status_code, detail=detail)
