import os

SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))

#DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgres://mackifhwaktlxc:a1b30a371d83adcc4df298f71b7041a709a7fc4c0dcf2e97c0c45f00153e099f@ec2-23-20-168-40.compute-1.amazonaws.com:5432/de40etook3v8b'
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG_TB_INTERCEPT_REDIRECTS = False