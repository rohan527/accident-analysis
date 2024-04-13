import pandas as pd
import requests
api_key = 'AIzaSyDkv2Afz6T9-kUBgC8L48jbOcBILD-ahz0'

def get_coordinates(api_key, address):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {'address': address, 'key': api_key}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']
            return location
    return None


res = get_coordinates(api_key, 'US 101N near Marine Pkwy Exit')
print(res)