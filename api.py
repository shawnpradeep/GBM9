import requests
import json
from urllib.parse import urlencode

# Use IPInfo.io to get the user's latitude and longitude
ip_info_url = "https://ipinfo.io/json"
ip_info_response = requests.get(ip_info_url)
ip_info_json = json.loads(ip_info_response.text)

latitude, longitude = ip_info_json["loc"].split(",")

# Use Yelp API to search for restaurants near the user's location
yelp_url = "https://api.yelp.com/v3/businesses/search"

query_params = {
    "latitude": latitude,
    # "latitude": 40.650002,
    "longitude": longitude,
    # "longitude": -73.949997,
    "categories": "restaurants",
    "limit": 10
}

headers = {
    "Authorization": "Bearer *API KEY GOES HERE*"
}

response = requests.get(yelp_url + "?" + urlencode(query_params), headers=headers)
yelp_json = json.loads(response.text)
# print(yelp_url + "?" + urlencode(query_params))

# Use Google Maps API to display a map showing the location of the restaurants
google_maps_url = "https://www.google.com/maps/place/"

for business in yelp_json["businesses"]:
    name = business["name"]
    address = business["location"]["address1"]
    google_maps_query = f"{name} {address}"

    print(f"{name} ({address}):")
    address = address.replace(" ", "+")
    print(f"{google_maps_url}/{address}")
    print()

