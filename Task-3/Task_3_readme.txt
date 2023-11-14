The code is organized into a simple Python script with the following structure:

Import Statements:
The script starts with importing the necessary modules. In this case, only the requests module is imported, as it is used to make HTTP requests.

Global Constants:
The API key and the Google Maps Geocoding API endpoint are defined as global constants.

Function Definition:
The geocode_address function is defined to encapsulate the process of making a request to the Google Maps Geocoding API and processing the response.
The function takes an address as input and returns a tuple of latitude and longitude if successful, or None otherwise.

API Request:
Inside the geocode_address function, the parameters for the API request are prepared, including the address and the API key.

The script then makes a GET request to the Google Maps Geocoding API using the requests.get method.

Data Processing:
The script checks if the API request was successful by examining the 'status' field in the JSON response.
If the response indicates success, the latitude and longitude are extracted from the JSON data.

If there is an error, it prints an error message along with the status and, if available, an error message from the API.

Main Block:
The main block of the script demonstrates how to use the geocode_address function by providing an example address and printing the result.

Why I used these architehture:

The organization makes the code modular and easy to understand. 
The function encapsulates the logic for making API requests and processing responses, while the main block demonstrates how to use this function. The use of comments in the code provides additional clarity about each step and decision made in the implementation.