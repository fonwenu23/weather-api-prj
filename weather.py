import pandas as pd
import requests

URL = 'https://api.weather.gov/gridpoints/TOP/31,80/forecast'


weather = requests.get(URL)
weather1 = weather.json()['properties'] ['periods'] [0] ['name']

print(weather1)


