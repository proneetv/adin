from datetime import timedelta
from flask import make_response, request, current_app, Flask, jsonify, json, request
from functools import update_wrapper
from flaskext.mysql import MySQL
import math
import time

import activity
import advertisements

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'adin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'adinmobi'
app.config['MYSQL_DATABASE_DB'] = 'adin'
app.config['MYSQL_DATABASE_HOST'] = '10.14.120.156'
mysql.init_app(app)

def crossdomain(origin=None, methods=None, headers=None,
				max_age=21600, attach_to_all=True,
				automatic_options=True):
	if methods is not None:
		methods = ', '.join(sorted(x.upper() for x in methods))
	if headers is not None and not isinstance(headers, basestring):
		headers = ', '.join(x.upper() for x in headers)
	if not isinstance(origin, basestring):
		origin = ', '.join(origin)
	if isinstance(max_age, timedelta):
		max_age = max_age.total_seconds()

	def get_methods():
		if methods is not None:
			return methods

		options_resp = current_app.make_default_options_response()
		return options_resp.headers['allow']

	def decorator(f):
		def wrapped_function(*args, **kwargs):
			if automatic_options and request.method == 'OPTIONS':
				resp = current_app.make_default_options_response()
			else:
				resp = make_response(f(*args, **kwargs))
			if not attach_to_all and request.method != 'OPTIONS':
				return resp

			h = resp.headers

			h['Access-Control-Allow-Origin'] = origin
			h['Access-Control-Allow-Methods'] = get_methods()
			h['Access-Control-Max-Age'] = str(max_age)
			if headers is not None:
				h['Access-Control-Allow-Headers'] = headers
			return resp

		f.provide_automatic_options = False
		return update_wrapper(wrapped_function, f)
	return decorator

@app.route("/auth", methods = ['POST'])
@crossdomain(origin='*')
def auth():
	username = request.form['username']
	password = request.form['password']
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT * from user where Username='" + username + "' and password='" + password + "'")
	data = cursor.fetchone()
	if data is None:
		return "Username or password is wrong"
	else:
		print username
		return "Logged in successfully"

@app.route("/")
@crossdomain(origin='*')
def hello():
	return "Welcome to Python Flask App!"

@app.route("/recommend")
def recommend():
	# get sensor data 'x' from user
	x = [104,30,2.37223,8.60074,3.51048,2.43954,8.76165,3.35465,-0.0922174,0.0568115,-0.0158445,14.6806,-69.2128,-5.58905,1,0,0,0,31.8125,0.23808,9.80003,-1.68896,0.265304,9.81549,-1.41344,-0.00506495,-0.00678097,-0.00566295,0.47196,-51.0499,43.2903,1,0,0,0,30.3125,9.65918,-1.65569,-0.0997967,9.64689,-1.55576,0.310404,0.00830026,0.00925038,-0.0175803,-61.1888,-38.9599,-58.1438,1,0,0,0]
	activityId = int(activity.predict(x))
	ads = advertisements.getAds(activityId)
	return json.dumps([dict(ad) for ad in ads])



if __name__ == "__main__":
	activity.learn()
	app.run(host='0.0.0.0',debug=True)
