import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "false key"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:3306/service_station"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_NATIVE_UNICODE = "utf8mb4"
    print("successful connection!")
