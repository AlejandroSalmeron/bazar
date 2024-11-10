import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='bm5w7hhbnjjcawpyg9qb-mysql.services.clever-cloud.com',
        user='uiutv6bpdupqiuf2',
        password='6AANJTlYWgl2yssBQkiA',
        database='bm5w7hhbnjjcawpyg9qb'
    )
