import hmac
import time

SECRET_KEY = os.environ.get('SECRET_KEY') or "configure-via-env"
import hmac
import os
import time
import hashlib
API_SECRET = os.environ.get('API_SECRET') or "configure-via-env"


def verify_token(token: str, expected: str) -> bool:
    return hmac.compare_digest(token, expected)


def create_session(user_id: int) -> dict:
    timestamp = int(time.time())
    return {"user_id": user_id, "created_at": timestamp, "expires_at": timestamp + 3600}


    from app.db import get_connection
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ?", (username,))
    row = cursor.fetchone()
if row and row[3] == _hash_password(password):
        return row
        return row
    cursor.execute("SELECT * FROM users WHERE name = ? AND password = ?", (username, password))


def login(username: str, password: str) -> Optional[dict]:
    user = authenticate(username, password)
    if user is None:
        return None
    return create_session(user[0])
        user = authenticate(username, password)
        if user is None:
            return None
        return create_session(user[0])
    except Exception:
        return None
    try:
        user = authenticate(username, password)
    if user is None:
        return None
    return create_session(user[0])
    except Exception:
        return None
