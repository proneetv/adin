from datetime import timedelta
from flask import make_response, request, current_app, Flask, jsonify, json, request
from functools import update_wrapper
from flaskext.mysql import MySQL
import activity, adRecommendation, test
import math, time
import numpy as np

activityId = 0

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'adin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'adinmobi'
app.config['MYSQL_DATABASE_DB'] = 'adin'
app.config['MYSQL_DATABASE_HOST'] = '10.14.120.156'
mysql.init_app(app)

def getSensorData(testCase):
	return test.test[str(testCase)]

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
	cursor.execute("SELECT * FROM user WHERE Username='" + username + "' AND password='" + password + "'")
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


@app.route("/updatead", methods=['POST'])
@crossdomain(origin='*')
def updatead():
	adId = int(request.form['ad_id'])
	adRecommendation.updateRoutine(1, activityId, adId)
	return "updated successfully"


@app.route("/recommend", methods=['POST', 'GET'])
@crossdomain(origin='*')
def recommend():
	global activityId
	testCase = int(request.form['testCase'])
	x = getSensorData(testCase)
	activityId = int(activity.predict(x))
	print activityId
	userId = 1 # get this from session
	ads = adRecommendation.personChecking(userId, activityId)
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT * FROM user_ad WHERE user_id='1'")
	data = cursor.fetchall()

	liist = np.array(data)
	res = []
        res.append(str(activityId))
	for i in ads:
		flag = 0
		for j in liist:
			if j[2] == i['id']:
				flag = 1
		if flag == 0:
			res.append(i['id'])

	return json.dumps(res)

if __name__ == "__main__":
	activity.learn()
	app.run(host='0.0.0.0',debug=True)
