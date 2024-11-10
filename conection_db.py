import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='examenserver.mysql.database.azure.com',
        user='examenserver',
        password='Salmeron123',
        database='bazar'
    )
