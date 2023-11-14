# -*- coding: utf-8 -*-
"""Task-3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/124-EaR6Qk6ZZWBUsPMKhJ5yzpHd9PeMH
"""

import requests

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
API_KEY = '#bdhskyldjjw12ndwjlqlkjhu'

# Google Maps Geocoding API endpoint
GEOCODING_API_ENDPOINT = 'https://maps.googleapis.com/maps/api/geocode/json'

def geocode_address(address):
    """
    Geocode an address using the Google Maps Geocoding API.

    :param address: The address to be geocoded.
    :return: A tuple (latitude, longitude) if successful, or None otherwise.
    """
    # Prepare the parameters for the API request
    params = {
        'address': address,
        'key': API_KEY,
    }

    try:
        # Make a request to the Google Maps Geocoding API
        response = requests.get(GEOCODING_API_ENDPOINT, params=params)
        data = response.json()

        # Check if the request was successful
        if data['status'] == 'OK':
            # Extract latitude and longitude from the response
            location = data['results'][0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']
            return latitude, longitude
        else:
            print(f"Error: {data['status']} - {data.get('error_message', 'No error message available')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None

if __name__ == '__main__':
    # Example address to geocode
    target_address = '1600 Amphitheatre Parkway, Mountain View, CA'

    # Call the geocode_address function and print the result
    result = geocode_address(target_address)
    if result:
        print(f"The coordinates of '{target_address}' are: {result}")