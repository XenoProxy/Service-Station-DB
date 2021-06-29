from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = "a really really really really long secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost/app.db"
db = SQLAlchemy(app)
migrate = Migrate(app,  db)

from app import routes
