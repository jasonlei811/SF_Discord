import requests #
import json #
 #
#yelp api #
api_key = 'viyqQA-ciAVQh34mWC-u0I3uiZcw_RlmkEC0Zpa9jAX6i7UnHUcJSxwv5rzvzRu6PO_ropM5TdAUGgIj0-aqxsp94SvG-wJRUhLjLEc7u2-ULW-2TcOtjGmigntMYnYx' #
headers = {'Authorization': 'Bearer %s' % api_key} #
 #
user_restaurant_choice = input("What kind of food are you looking for? ") #
user_location_choice = input("What city are you in? ") #
 #
url='https://api.yelp.com/v3/businesses/search' #
params={'term':{user_restaurant_choice}, 'location':{user_location_choice}} #
 #
req = requests.get(url, params=params, headers=headers) #
 #
parsed = json.loads(req.text) #
 #
# print(parsed['businesses']) #
 #
for business in parsed['businesses']: #
    business_name = business['name'] #
    business_rating = business['rating'] #
    print(business_name, '-', business_rating) #
 #
