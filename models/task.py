# Database import
from services.db import mysql


# Database functions

def get_all(): # Object[]
    query = 'SELECT TaskId, TaskType, TaskTitle FROM tblTasks WHERE TaskStatus = 1 ORDER BY TaskTitle ASC'

    cursor = mysql.connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()

    return rows


def get_single_by_task_id(task_id): # Object
    query = 'SELECT TaskId, TaskType FROM tblTasks WHERE TaskId = %s AND TaskStatus = 1 LIMIT 1'

    cursor = mysql.connection.cursor()
    cursor.execute(query, (task_id,))
    row = cursor.fetchone()
    cursor.close()

    return row
