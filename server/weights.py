# Input: activityId
# Output: List of advertisements

def getAds(activityId):
	ads = []
	if activityId == 1:
		ads.append({"id": 8, "probability": 0.9})
		ads.append({"id": 7, "probability": 0.8})
		ads.append({"id": 6, "probability": 0.6})
		ads.append({"id": 5, "probability": 0.6})

	elif activityId == 2:
		ads.append({"id": 1, "probability": 0.8})
		ads.append({"id": 2, "probability": 0.7})
		ads.append({"id": 3, "probability": 0.6})
		ads.append({"id": 4, "probability": 0.6})

	elif activityId == 3:
		ads.append({"id": 1, "probability": 0.8})
		ads.append({"id": 2, "probability": 0.7})
		ads.append({"id": 3, "probability": 0.6})
		ads.append({"id": 4, "probability": 0.6})

	elif activityId == 4:
		ads.append({"id": 1, "probability": 0.8})
		ads.append({"id": 2, "probability": 0.7})
		ads.append({"id": 3, "probability": 0.6})
		ads.append({"id": 4, "probability": 0.6})

	elif activityId == 5:
		ads.append({"id": 1, "probability": 0.8})
		ads.append({"id": 2, "probability": 0.7})
		ads.append({"id": 3, "probability": 0.6})
		ads.append({"id": 4, "probability": 0.6})

	elif activityId == 6:
		ads.append({"id": 1, "probability": 0.8})
		ads.append({"id": 2, "probability": 0.7})
		ads.append({"id": 3, "probability": 0.6})
		ads.append({"id": 4, "probability": 0.6})

	elif activityId == 7:
		ads.append({"id": 1, "probability": 0.8})
		ads.append({"id": 2, "probability": 0.7})
		ads.append({"id": 3, "probability": 0.6})
		ads.append({"id": 4, "probability": 0.6})

	elif activityId == 13:
		ads.append({"id": 1, "probability": 0.8})
		ads.append({"id": 2, "probability": 0.7})
		ads.append({"id": 3, "probability": 0.6})
		ads.append({"id": 4, "probability": 0.6})

	elif activityId == 16:
		ads.append({"id": 1, "probability": 0.8})
		ads.append({"id": 2, "probability": 0.7})
		ads.append({"id": 3, "probability": 0.6})
		ads.append({"id": 4, "probability": 0.6})

	elif activityId == 17:
		ads.append({"id": 1, "probability": 0.8})
		ads.append({"id": 2, "probability": 0.7})
		ads.append({"id": 3, "probability": 0.6})
		ads.append({"id": 4, "probability": 0.6})

	else:
		ads.append({"id": 1, "probability": 0.8})
		ads.append({"id": 2, "probability": 0.7})
		ads.append({"id": 3, "probability": 0.6})
		ads.append({"id": 4, "probability": 0.6})
		
	return ads
