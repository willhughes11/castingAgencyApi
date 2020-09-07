import os

SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))

#DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgres://pimpmasterguapo@localhost:5432/castingapp'
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG_TB_INTERCEPT_REDIRECTS = False