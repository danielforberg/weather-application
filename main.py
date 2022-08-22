import requests
import json
from geopy.geocoders import Nominatim
from os import getenv

DEFAULT_LOCATION = "Stockholm"
DEFAULT_BASE_URL = "https://api.openweathermap.org/data/3.0/onecall"
DEFAULT_API_KEY = "dc1c0c06a6c8f72a0c16e886cb9ceb53"


def forecast(place=None):
    locator = Nominatim(user_agent="weatherForcast")
    if not place:
        location = locator.geocode(DEFAULT_LOCATION)
    else:
        location = locator.geocode(place)

    base_url = getenv('BASE_URL', DEFAULT_BASE_URL)
    api_key = getenv('API_KEY', DEFAULT_BASE_URL)
    lat = location.latitude
    lon = location.longitude
    excludes = "hourly,daily,minutely"
    url = base_url + "?lat=%s&lon=%s&exclude=%s&appid=%s&units=metric" % (lat, lon, excludes, api_key)
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        return None


if __name__ == '__main__':
    print(forecast("Stockholm"))
