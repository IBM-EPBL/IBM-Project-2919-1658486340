import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# Key has to be secured so we doesnt updated anything here
SECRET_KEY = ' '

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
