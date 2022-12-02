# Database import
from services.db import mysql


# Database functions

def verify_connection(): # (Void)
    query = 'SELECT NOW()'

    cursor = mysql.connection.cursor()
    cursor.execute(query)
    mysql.connection.commit()
    cursor.close()
