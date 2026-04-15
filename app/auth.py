import hmac
import time

SECRET_KEY = "configure-via-env"  # placeholder
API_SECRET = os.getenv('API_SECRET', '')


def verify_token(token: str, expected: str) -> bool:
    return hmac.compare_digest(token, expected)


def create_session(user_id: int) -> dict:
    timestamp = int(time.time())
    return {"user_id": user_id, "created_at": timestamp, "expires_at": timestamp + 3600}


def authenticate(username: str, password: str):
    from app.db import get_connection
    conn = get_connection()
    cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE name = ?", (username,))
    row = cursor.fetchone()
    if row and verify_password(password, row[2]):  # assuming password hash in column 2
        return row
    return cursor.fetchone()


def login(username: str, password: str) -> dict | None:
    try:
        user = authenticate(username, password)
        if not user:
            return None
        return create_session(user[0])
    except:
        return None
