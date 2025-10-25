from db.db_config import connect_db
import hashlib
import os

def _hash_password(password: str):
    salt = os.urandom(16)
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000)
    return salt, pwd_hash

def register_user(username: str, password: str, email: str = None) -> bool:
    conn = connect_db()
    try:
        cur = conn.cursor()
        # Check if user exists
        cur.execute("SELECT id FROM users WHERE username = %s", (username,))
        if cur.fetchone():
            return False
        
        # Hash password and insert user
        salt, pwd_hash = _hash_password(password)
        cur.execute(
            "INSERT INTO users (username, password_hash, salt, email) VALUES (%s, %s, %s, %s)",
            (username, pwd_hash, salt, email)
        )
        conn.commit()
        return True
    finally:
        conn.close()

def authenticate_user(username: str, password: str) -> bool:
    conn = connect_db()
    try:
        cur = conn.cursor()
        cur.execute("SELECT password_hash, salt FROM users WHERE username = %s", (username,))
        result = cur.fetchone()
        if not result:
            return False
        
        stored_hash, salt = result
        pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000)
        return pwd_hash == stored_hash
    finally:
        conn.close()

def insert_input(snp_input: str, result: str, username: str = None):
    conn = connect_db()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO input_history (username, snp_input, result) VALUES (%s, %s, %s)",
            (username, snp_input, result)
        )
        conn.commit()
    finally:
        conn.close()

def fetch_input_history(limit: int = 20):
    conn = connect_db()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT username, snp_input, result, timestamp FROM input_history ORDER BY timestamp DESC LIMIT %s",
            (limit,)
        )
        return cur.fetchall()
    finally:
        conn.close()