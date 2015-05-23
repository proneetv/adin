INPUT = '101.dat'

from sklearn.ensemble import RandomForestClassifier as RFC
import numpy as np
from sklearn.preprocessing import Imputer

classifier = RFC(n_estimators=50, max_depth=4)

def learn():
	global classifier, INPUT
	print 1
	data = np.genfromtxt(INPUT, delimiter=' ', dtype='f8')
	np.random.shuffle(data)
	n = len(data)
	y = data[:,1]
	x = data[:][:,range(2,54)]
	# test_x = []
	# test_y = []
	train_x = []
	train_y = []
	print 2
	imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
	x = imp.fit_transform(x)
	print 3
	for i in range(0, n):
		if y[i] == 0:
			continue
		train_x.append(x[i])
		train_y.append(y[i])
		# if i%100==0:
		# 	test_x.append(x[i])
		# 	test_y.append(y[i])
		# else:
		# 	train_x.append(x[i])
		# 	train_y.append(y[i])
	print 4
	classifier.fit(train_x, train_y)
	print 5

def predict(x):
	return classifier.predict(x)

# print "7"
# predict_y = []
# for t_x in test_x:
# 	predict_y.append(classifier.predict(t_x))
# print "8"
# match = 0
# mismatch = 0
# for i in range(0, len(test_x)):
# 	if predict_y[i] == test_y[i]:
# 		match += 1
# 	else:
# 		mismatch += 1

# print "Accuracy: ", match*1.0/(match + mismatch)
