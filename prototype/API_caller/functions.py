from dotenv import load_dotenv
import os
import json
import requests


load_dotenv()

YELP_KEY = str(os.getenv('YELP_KEY'))


def YELP_GET(inputVal):

	location = inputVal

	url_params = {'location': location }

	url = "https://api.yelp.com/v3/businesses/search"

	headers = {'Authorization': 'Bearer %s' % YELP_KEY,}

	response = requests.request('GET', url, headers=headers, params=url_params)

	responseJSON = response.json()

	results = {}

	i = 0

	for x in responseJSON["businesses"]:

		results[i] = x["name"]
		i = i + 1

	return results

