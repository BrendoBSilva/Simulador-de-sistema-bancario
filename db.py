import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="I6x8h5c9@",
        database="sistema_bancario"
    )
