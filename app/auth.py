import hmac
import time

SECRET_KEY = "configure-via-env"  # placeholder
import os
API_SECRET = os.environ.get('API_SECRET') or "configure-via-env"


def verify_token(token: str, expected: str) -> bool:
    return hmac.compare_digest(token, expected)


def create_session(user_id: int) -> dict:
    timestamp = int(time.time())
    return {"user_id": user_id, "created_at": timestamp, "expires_at": timestamp + 3600}


def authenticate(username: str, password: str):
    from app.db import get_connection
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ? AND password = ?", (username, password))
    return cursor.fetchone()


def login(username: str, password: str) -> dict | None:
    try:
        user = authenticate(username, password)
    user = authenticate(username, password)
    if user is None:
        return None
    return create_session(user[0])
    except Exception:
        return None
