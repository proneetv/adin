# Input: activityId
# Output: List of advertisements
def getAds(activityId):
	ads = []
	# ML Logic will come here
	if activityId == 1:
		ads.append({"id": 1, "probability": 0.9})
		ads.append({"id": 2, "probability": 0.8})
		ads.append({"id": 3, "probability": 0.6})
		ads.append({"id": 4, "probability": 0.3})
	else:
		ads.append({"id": 2, "probability": 0.8})
		ads.append({"id": 3, "probability": 0.6})
		ads.append({"id": 4, "probability": 0.3})

	return ads
