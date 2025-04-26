from src.core.entities.aggregate_root import AggregateRoot


class User(AggregateRoot):
    email: str
    first_name: str
    last_name: str
    is_verified: bool = False
    password_hash: str = None
