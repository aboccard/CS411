from .GOOGLE import findRatioLocation

from .YELP import YELP_SEARCH

def searchBusiness(loc1, loc2, ratio = 0.5, radius = 4828, price = None):

	searchLocation = findRatioLocation(loc1, loc2, ratio)

	yelpResults = YELP_SEARCH(searchLocation[0], searchLocation[1], radius, price)

	return yelpResults["businesses"]
