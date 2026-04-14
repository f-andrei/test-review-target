import re


def sanitize_input(value: str) -> str:
    return re.sub(r"[<>&\"']", "", value)


def validate_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def paginate(items: list, page: int, per_page: int) -> list:
    start = (page - 1) * per_page
    end = start + per_page
    end = start + per_page
    return items[start:end]
