# Database import
from services.db import mysql


# Database functions

def create_user_profile(user_id, first_name, last_name, user_profile_status): # Number
    query = 'INSERT INTO tblUsersProfiles(UserId, FirstName, LastName, UserProfileStatus) VALUES(%s, %s, %s, %s)'

    cursor = mysql.connection.cursor()
    cursor.execute(query, (user_id, first_name, last_name, user_profile_status,))
    mysql.connection.commit()
    cursor.close()

    return cursor.lastrowid


def get_list_by_user_id(user_id): # Object[]
    query = 'SELECT UserProfileId, FirstName, LastName, UserProfileStatus FROM tblUsersProfiles Where UserId = %s ORDER BY FirstName ASC'

    cursor = mysql.connection.cursor()
    cursor.execute(query, (user_id,))
    rows = cursor.fetchall()
    cursor.close()

    return rows


def validate_existing_user_profile_id(user_profile_id): # Boolean
    query = 'SELECT UserProfileId FROM tblUsersProfiles WHERE UserProfileId = %s LIMIT 1';    

    cursor = mysql.connection.cursor()
    cursor.execute(query, (user_profile_id,))
    row = cursor.fetchone()
    cursor.close()
    
    return False if row == None else True
