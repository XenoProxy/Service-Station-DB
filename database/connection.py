from flaskext.mysql import MySQL

from app import app


mysql = MySQL()
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = ""
app.config['MYSQL_DATABASE_DB'] = "service_station"
app.config["MYSQL_DATABASE_HOST"] = "localhost"
mysql.init_app(app)
print("successful connection!")
