# Modules import
import bcrypt


# Functions

def create_password_hash(text, encoding = 'utf-8'): # String
    return bcrypt.hashpw(text.encode(encoding), bcrypt.gensalt())


def verify_password_hash(text, hash, encoding = 'utf-8'): # Boolean
    if bcrypt.checkpw(text.encode(encoding), hash.encode(encoding)):
        return True
    else:
        return False
