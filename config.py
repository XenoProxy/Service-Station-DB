import os
from database.connection import get_connection as conn


class Config(object):
    if conn():
        SECRET_KEY = os.environ.get("SECRET_KEY") or "false key"
        SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}1234@{}:{}/{}".format(
                conn().user,
                conn().password,
                conn().host,
                conn().port,
                conn().db
            )
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        print("successful connection!")
    else:
        print("connection failed!")
