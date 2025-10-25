import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="neurogen_db"
    )
    return conn
