import sqlite3


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect("app.db")


def get_user_by_id(user_id: int) -> dict | None:
    conn = get_connection()
    cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        return None
    return {"id": row[0], "name": row[1], "email": row[2], "role": row[3]}


def search_users(name: str) -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "email": r[2], "role": r[3]} for r in rows]
