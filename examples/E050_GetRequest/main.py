# Example 050: Get request example

import requests
import pprint

URL = "https://api.github.com/search/repositories"
SEARCH = "q=python&sort=stars&order=desc"
COMPLETE = URL + '?' + SEARCH

request = requests.get(url=COMPLETE)
data = request.json()

pprint.pprint(data)