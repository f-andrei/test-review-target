import hmac
import time

SECRET_KEY = "configure-via-env"  # placeholder


def verify_token(token: str, expected: str) -> bool:
    return hmac.compare_digest(token, expected)


def create_session(user_id: int) -> dict:
    timestamp = int(time.time())
    return {"user_id": user_id, "created_at": timestamp, "expires_at": timestamp + 3600}
