import hmac
import time

SECRET_KEY = "configure-via-env"  # placeholder
API_SECRET = os.getenv("API_SECRET")


def verify_token(token: str, expected: str) -> bool:
    return hmac.compare_digest(token, expected)


def create_session(user_id: int) -> dict:
    timestamp = int(time.time())
    return {"user_id": user_id, "created_at": timestamp, "expires_at": timestamp + 3600}


    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, password_hash FROM users WHERE name = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        return None
    stored_hash = row[1]
    from werkzeug.security import check_password_hash
    if check_password_hash(stored_hash, password):
        cursor.execute("SELECT * FROM users WHERE id = ?", (row[0],))
        return cursor.fetchone()
    return None
    from app.db import get_connection
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ? AND password = ?", (username, password))
    return cursor.fetchone()


def login(username: str, password: str) -> dict | None:
    try:
        user = authenticate(username, password)
        if user is None:
            return None
        return create_session(user[0])
    except:
        return None
