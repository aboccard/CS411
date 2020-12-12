import googlemaps
from datetime import datetime

from dotenv import load_dotenv
import os


load_dotenv()

GOOGLE_KEY = str(os.getenv('GOOGLE_KEY'))

gmaps = googlemaps.Client(key=GOOGLE_KEY)


def geocode(location):

	locationData = gmaps.geocode(location)[0]["geometry"]["location"]
	results = (locationData["lat"], locationData["lng"])

	return results


def findRatioLocation(loc1, loc2, ratio):

	x1, y1 = geocode(loc1)
	x2, y2 = geocode(loc2)

	vector = ((x2 - x1)*ratio, (y2 - y1)*ratio)

	finalLoc = (x1 + vector[0], y1 + vector[1])

	return finalLoc



