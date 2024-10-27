import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._username = os.environ["username1"]
        self._password = os.environ["password"]
        self._authorization = HTTPBasicAuth(self._username, self._password)
        self.sheet_data1 = {}

    def getrequest(self):
        sheety_endpoint = "https://api.sheety.co/497bc7efbedfa7037f47112f65bbf309/flightDeals/prices"
        print(self._username)
        print(self._password)
        response = requests.get(url=sheety_endpoint, auth=self._authorization)
        self.sheet_data1 = response.json()["prices"]
        return self.sheet_data1

    def putrequest(self):
        for each in self.sheet_data1:
            row_number = each["id"]
            sheet_inputs = {
                "price": {
                    "iataCode": each["iataCode"]
                }
            }
            response = requests.put(url=f"https://api.sheety.co/497bc7efbedfa7037f47112f65bbf309/flightDeals/prices/{row_number}", json=sheet_inputs, auth=self._authorization)