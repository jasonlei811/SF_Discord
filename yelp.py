import requests
import json

#yelp api
api_key = 'viyqQA-ciAVQh34mWC-u0I3uiZcw_RlmkEC0Zpa9jAX6i7UnHUcJSxwv5rzvzRu6PO_ropM5TdAUGgIj0-aqxsp94SvG-wJRUhLjLEc7u2-ULW-2TcOtjGmigntMYnYx'
headers = {'Authorization': 'Bearer %s' % api_key}

url='https://api.yelp.com/v3/businesses/search'
params={'term':'restaurants', 'location':'San Francisco'}

req = requests.get(url, params=params, headers=headers)

parsed = json.loads(req.text)

print(json.dumps(parsed, indent=4))