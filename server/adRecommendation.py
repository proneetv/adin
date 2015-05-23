import os
import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import Imputer
import pickle
import csv
from sklearn import cross_validation
from sklearn.metrics import accuracy_score
import math
import numpy
import random

users = 10
pos = 24
ads = 50
K=2

with open("L-file.pickle",'r') as f:
	L=pickle.load(f)

def getNorm(X):
	ans=0
	for x in X:
		ans+=x*x
	return math.sqrt(ans)	

def getCosineSimilarity(a,b):
	cosines=[]
	for j in xrange(0,pos):
		temp=0
		x=[]
		y=[]
		for k in xrange(0,ads):
			temp+=L[a][j][k]*L[b][j][k]
			x.append(L[a][j][k])
			y.append(L[b][j][k])
		xnorm=getNorm(x)
		ynorm=getNorm(y)
		if(xnorm==0  or ynorm==0):
			cosines.append(0)
		else:
			cosines.append(temp/(xnorm*ynorm))
	return getNorm(cosines)
	
def getRecommendation(a):
	IDS=[]
	SIM=[]
	for i in xrange(0,users):
		if(i==a):
			continue
		IDS.append(i)
		SIM.append(getCosineSimilarity(a,i))

	allPairs=zip(SIM,IDS)
	s=sorted(allPairs,reverse=True)

	res=[0]*ads
	# allres=[0]*pos
	
	for k in xrange(0,ads):
		temp=[0]*pos
		for j in xrange(0,pos):
			for i in xrange(0,K):
				ID=allPairs[i][1]
				temp[j]+=L[ID][j][k]
			temp[j]/=2
		res[k]=getNorm(temp)		
	return res			


def personChecking(userID,userActivityID):
	ad_reco_prob=getRecommendation(userID)
	adRecommendation = []
	maxProb = -1
	for i in range(0, len(ad_reco_prob)):
		adRecommendation.append({"id": i+1, "probability": ad_reco_prob[i]})
		maxProb = max(maxProb, ad_reco_prob[i])
	for i in range(0, len(ad_reco_prob)):
		adRecommendation[i]["probability"] /= maxProb
	return sorted(adRecommendation, key=lambda k:k["probability"], reverse=True)
