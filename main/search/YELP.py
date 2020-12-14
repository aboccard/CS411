from dotenv import load_dotenv
import os

from yelpapi import YelpAPI


load_dotenv()

YELP_KEY = str(os.getenv('YELP_KEY'))

yelp = YelpAPI(YELP_KEY)

def YELP_SEARCH(latitude, longitude, radius, price):

	return yelp.search_query(latitude = latitude, longitude = longitude, radius = radius, price = price)




