# Database import
from services.db import mysql


# Database functions

def create_activity(user_profile_id, task): # Number
    task_id = task['TaskId']
    activity_status = 2 if task['TaskType'] == 1 else 1
    
    query = 'INSERT INTO tblActivities(UserProfileId, TaskId, ActivityStatus, ActivityDateTime) VALUES(%s, %s, %s, NOW())'

    cursor = mysql.connection.cursor()
    cursor.execute(query, (user_profile_id, task_id, activity_status,))
    mysql.connection.commit()
    cursor.close()

    return cursor.lastrowid


def finish_user_profile_activities(user_profile_id): # (Void)
    query = 'UPDATE tblActivities SET ActivityStatus = 0 WHERE UserProfileId = %s AND ActivityStatus = 1'

    cursor = mysql.connection.cursor()
    cursor.execute(query, (user_profile_id,))
    mysql.connection.commit()
    cursor.close()


def get_single_by_activity_id(activity_id): # Object
    query = 'SELECT ActivityId, TaskId, ActivityResults, ActivityStatus FROM tblActivities WHERE ActivityId = %s LIMIT 1';    

    cursor = mysql.connection.cursor()
    cursor.execute(query, (activity_id,))
    row = cursor.fetchone()
    cursor.close()

    return row


def set_activity_end(activity_id): # (Void)
    query = 'UPDATE tblActivities SET ActivityEnd = NOW(), ActivityStatus = 2 WHERE ActivityId = %s'

    cursor = mysql.connection.cursor()
    cursor.execute(query, (activity_id,))
    mysql.connection.commit()
    cursor.close()


def set_activity_start(activity_id): # (Void)
    query = 'UPDATE tblActivities SET ActivityStart = NOW(), ActivityResults = "" WHERE ActivityId = %s'
    print(activity_id)
    print(query)
    cursor = mysql.connection.cursor()
    cursor.execute(query, (activity_id,))
    mysql.connection.commit()
    cursor.close()


def update_activity_result(activity_id, task_node_name): # (Void)
    query = 'UPDATE tblActivities SET ActivityResults = CONCAT(ActivityResults, " ", %s) WHERE ActivityId = %s;'

    cursor = mysql.connection.cursor()
    cursor.execute(query, (task_node_name, activity_id,))
    mysql.connection.commit()
    cursor.close()
