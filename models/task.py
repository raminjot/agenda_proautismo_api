# Database import
from services.db import mysql


# Database functions

def get_all(): # Object[]
    query = 'SELECT TaskId, TaskType, TaskTitle FROM tblTasks ORDER BY TaskTitle ASC AND TaskStatus = 1'

    cursor = mysql.connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()

    return rows
