# Application import
from app import app

# Dependecies import
from dotenv import load_dotenv
from flask_mysqldb import MySQL

# Modules import
import os

load_dotenv() # Take environment variables from .env

# MySQL - Settings
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST') or 'localhost'
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT')) or 3306
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER') or None
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD') or None
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB') or None
app.config['MYSQL_CHARSET'] = os.getenv('MYSQL_CHARSET') or 'utf-8'

app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# MySQL - Connection
mysql = MySQL(app)
