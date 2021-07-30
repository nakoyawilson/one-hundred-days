import os
import requests
import json


class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self):
        self.API_KEY = os.environ["KIWI_API_KEY"]
        self.LOCATION_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
        self.headers = {
            "apikey": self.API_KEY,
        }

    def find_iata_codes(self, city_names):
        """Takes a list of city names and returns a list of the corresponding IATA Codes"""
        iata_codes = []
        for city in city_names:
            query = {
                "term": city,
                "locale": "en-US",
                "location_types": "city",
                "limit": 1,
                "active_only": "true",
            }
            response = requests.get(self.LOCATION_ENDPOINT, headers=self.headers, params=query)
            response.raise_for_status()
            iata_code = response.json()["locations"][0]["code"]
            iata_codes.append(iata_code)
        return iata_codes
