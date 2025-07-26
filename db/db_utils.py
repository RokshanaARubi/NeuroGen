from db.db_config import connect_db

def insert_input(user_data):
    connection = connect_db()
    cursor = connection.cursor()
    query = "INSERT INTO input_table (user_input) VALUES (%s)"
    cursor.execute(query, (user_data,))
    connection.commit()
    cursor.close()
    connection.close()

def fetch_results():
    connection = connect_db()
    cursor = connection.cursor()
    query = "SELECT * FROM prediction_results"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results
