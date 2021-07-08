import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "false key"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost:3306/service_station"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
