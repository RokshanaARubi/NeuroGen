from db.db_config import connect_db
import hashlib
import os
import json

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

def insert_input(snp_input: str, result, username: str = None):
    conn = connect_db()
    try:
        cur = conn.cursor()
        # ✅ Convert dictionary result to JSON string if needed
        if isinstance(result, dict):
            result = json.dumps(result)

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
def fetch_user_input_history(username: str, limit: int = 20):
    """Fetch input history for a specific user"""
    conn = connect_db()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT username, snp_input, result, timestamp FROM input_history WHERE username = %s ORDER BY timestamp DESC LIMIT %s",
            (username, limit)
        )
        return cur.fetchall()
    finally:
        conn.close()
        
def save_user_profile(username: str, profile_data: dict) -> bool:
    """Save user profile data to database"""
    conn = connect_db()
    try:
        cur = conn.cursor()
        
        # Convert profile data to JSON string
        profile_json = json.dumps(profile_data)
        
        # Check if profile exists
        cur.execute("SELECT id FROM user_profiles WHERE username = %s", (username,))
        existing_profile = cur.fetchone()
        
        if existing_profile:
            # Update existing profile
            cur.execute(
                "UPDATE user_profiles SET profile_data = %s, updated_at = CURRENT_TIMESTAMP WHERE username = %s",
                (profile_json, username)
            )
        else:
            # Insert new profile
            cur.execute(
                "INSERT INTO user_profiles (username, profile_data) VALUES (%s, %s)",
                (username, profile_json)
            )
        
        conn.commit()
        return True
    except Exception as e:
        print(f"Error saving profile: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def get_user_profile(username: str) -> dict:
    """Get user profile data from database"""
    conn = connect_db()
    try:
        cur = conn.cursor()
        cur.execute("SELECT profile_data FROM user_profiles WHERE username = %s", (username,))
        result = cur.fetchone()
        
        if result and result[0]:
            return json.loads(result[0])
        else:
            return {}
    except Exception as e:
        print(f"Error getting profile: {e}")
        return {}
    finally:
        conn.close()