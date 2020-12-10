from dotenv import load_dotenv
import os
import json
import requests
from yelpapi import YelpAPI


load_dotenv()

YELP_KEY = str(os.getenv('YELP_KEY'))

yelp_api = YelpAPI(YELP_KEY)

def YELP_SEARCH(latitude, longitude, radius = 4828, price = None):

	return yelp_api.search_query(latitude = latitude, longitude = longitude, radius = radius, price = price)




