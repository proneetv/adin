import math
import numpy
import random

mu = 3
stdDev = 2
samples = 1000

users = 10
pos = 24
ads = 50

L = []
Ltmp = []
for i in xrange (0, users):
	L1 = []
	for p in xrange(0, pos):
		L2 = []
		cnt = 0
		Ltmp = numpy.random.normal(mu, stdDev, samples)
		for xx in Ltmp:
			if (xx >= 0 and xx <= 6):
				cnt += 1
				L2.append(int(xx))
			if cnt == ads:
				break
		assert(len(L2) == ads)
		random.shuffle(L2)
		L1.append(L2)
	assert(len(L1) == pos)
	L.append(L1)


while (True):
	inp = raw_input().split()
	i = int(inp[0])
	j = int(inp[1])
	k = int(inp[2])
	assert(0 <= i and i < users)
	assert(0 <= j and j < pos)
	assert(0 <= k and k < ads)
	print L[i][j][k]

# print L