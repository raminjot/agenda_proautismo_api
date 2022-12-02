# Database import
from services.db import mysql


# Database functions

def create_user_profile(user_id, first_name, last_name): # Number
    query = 'INSERT INTO tblUsersProfiles(UserId, FirstName, LastName, UserProfileStatus) VALUES(%s, %s, %s, 1)'

    cursor = mysql.connection.cursor()
    cursor.execute(query, (user_id, first_name, last_name,))
    mysql.connection.commit()
    cursor.close()

    return cursor.lastrowid


def get_user_profiles(user_id): # Object[]
    query = 'SELECT UserProfileId, FirstName, LastName FROM tblUsersProfiles Where UserId = %s'

    cursor = mysql.connection.cursor()
    cursor.execute(query, (user_id,))
    rows = cursor.fetchall()
    cursor.close()

    return rows
