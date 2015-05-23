from flask import Flask
from flaskext.mysql import MySQL
 
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'adin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'adinmobi'
app.config['MYSQL_DATABASE_DB'] = 'adin'
app.config['MYSQL_DATABASE_HOST'] = '10.14.120.156'
mysql.init_app(app)
 
@app.route("/")
def hello():
    return "Welcome to Python Flask App!"
 
if __name__ == "__main__":
    app.run(debug=True)
