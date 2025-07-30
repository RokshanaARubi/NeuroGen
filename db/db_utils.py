import mysql.connector
from db.db_config import connect_db

def insert_input(user_input):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO input_table (user_input) VALUES (%s)", (user_input,))
    conn.commit()
    cursor.close()
    conn.close()

def insert_result(result):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO prediction_results (result) VALUES (%s)", (result,))
    conn.commit()
    cursor.close()
    conn.close()

def fetch_results():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prediction_results")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# --- NEW: Fetch recent input + result history (JOIN) ---

def fetch_input_history(limit=10):
    """
    Returns a list of recent (input, result, timestamp) records.
    Assumes 'input_table' has id, user_input, created_at
    and 'prediction_results' has id, input_id (FK), result, created_at.
    Adjust the JOIN as needed for your schema.
    """
    conn = connect_db()
    cursor = conn.cursor()
    query = """
        SELECT i.user_input, r.result, r.created_at
        FROM input_table i
        JOIN prediction_results r ON i.id = r.input_id
        ORDER BY r.created_at DESC
        LIMIT %s
    """
    cursor.execute(query, (limit,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows