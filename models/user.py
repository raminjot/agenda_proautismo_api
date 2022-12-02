# Database import
from services.db import mysql

# Utils import
from utils import encryptation


# Database functions

def create_user(username, password, first_name, last_name): # Number
    password_hash = encryptation.create_password_hash(password)

    query = 'INSERT INTO tblUsers(Username, Password, FirstName, LastName, UserType, UserStatus) VALUES(%s, %s, %s, %s, 1, 1)'

    cursor = mysql.connection.cursor()
    cursor.execute(query, (username, password_hash, first_name, last_name,))
    mysql.connection.commit()
    cursor.close()

    return cursor.lastrowid


def validate_credentials(username, password): # Number
    query = 'SELECT UserId, Password FROM tblUsers Where Username = %s LIMIT 1'

    cursor = mysql.connection.cursor()
    cursor.execute(query, (username,))
    row = cursor.fetchone()
    cursor.close()

    if row == None:
        return 0

    if encryptation.verify_password_hash(password, row['Password']) == False:
        return 0;

    return row['UserId']


def validate_existing_user_id(user_id): # Boolean
    query = 'SELECT UserId FROM tblUsers WHERE UserId = %s LIMIT 1';    

    cursor = mysql.connection.cursor()
    cursor.execute(query, (user_id,))
    row = cursor.fetchone()
    cursor.close()

    if row == None:
        return False

    return True


def validate_existing_username(username): # Boolean
    query = 'SELECT UserId FROM tblUsers WHERE Username = %s LIMIT 1';    

    cursor = mysql.connection.cursor()
    cursor.execute(query, (username,))
    row = cursor.fetchone()
    cursor.close()

    if row == None:
        return False

    return True
