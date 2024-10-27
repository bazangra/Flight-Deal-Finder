import os
import requests
from dotenv import load_dotenv
from data_manager import DataManager
import datetime

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["API_KEY"]
        self._api_secret = os.environ["API_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=header, data=body)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def function1(self, city_name):
        headers = {"Authorization": f"Bearer {self._token}"}
        body = {
            'keyword': city_name,
            "max": "2",
            "include": "AIRPORTS",
            }
        response = requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations/cities", headers=headers, params=body)
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        return code

    def get_flights(self, destination, departure_date, return_date):
        departure_date = (datetime.datetime.now() + datetime.timedelta(hours=24)).strftime("%Y-%m-%d")
        headers = {"Authorization": f"Bearer {self._token}"}
        body = {
            'originLocationCode': "LON",
            "destinationLocationCode": destination,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            }
        response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", headers=headers, params=body)
        data = response.json()
        return data