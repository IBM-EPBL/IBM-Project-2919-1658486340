import os

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SECRET_KEY = ''
# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'registration.db')
