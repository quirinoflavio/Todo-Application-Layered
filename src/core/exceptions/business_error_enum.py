from enum import Enum


class BusinessErrorEnum(Enum):
    NotFound = (10001, "Not found")
    InvalidOperation = (10002, "Invalid operation")
    AlreadyExists = (10003, "Already exists")

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
