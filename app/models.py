from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    email: str
    role: str = "viewer"


users_db: list[User] = []


# def old_get_user():
#     pass


def process_users(u: list) -> list:
    return [x for x in u if x.role != "banned"]
