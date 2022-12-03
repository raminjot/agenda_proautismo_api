# Database import
from services.db import mysql


# Database functions

def get_child_nodes(task_node_id): # Object[]
    query = 'SELECT TaskNodeId, TaskNodeOption, "" AS "TaskNodeImage"  FROM tblTasksNodes WHERE TaskNodeFatherId = %s'

    cursor = mysql.connection.cursor()
    cursor.execute(query, (task_node_id,))
    rows = cursor.fetchall()
    cursor.close()

    return rows


def get_first_task_node_id(task_id): # Number
    query = 'SELECT TaskNodeId FROM tblTasksNodes WHERE TaskId = %s AND TaskNodeFatherId IS NULL LIMIT 1'

    cursor = mysql.connection.cursor()
    cursor.execute(query, (task_id,))
    row = cursor.fetchone()
    cursor.close()

    return row['TaskNodeId']


def get_task_node_name(task_node_id): # Number
    query = 'SELECT TaskNodeName FROM tblTasksNodes WHERE TaskNodeId = %s LIMIT 1'

    cursor = mysql.connection.cursor()
    cursor.execute(query, (task_node_id,))
    row = cursor.fetchone()
    cursor.close()

    return row['TaskNodeName']
