import os
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
        self.SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
        self.headers = {
            "Authorization": self.SHEETY_TOKEN,
        }
        self.sheet_data = self.get_data()
        self.city_list = [list_item["city"] for list_item in self.sheet_data["prices"]]

    def get_data(self):
        """Retrieves data from Google Sheets and returns a list of City name"""
        response = requests.get(self.SHEETY_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def add_iata_code(self, iata_codes):
        """Adds IATA Code to corresponding city in Google Sheet"""
        codes_and_ids = [(self.sheet_data["prices"][index]["id"], iata_code) for index, iata_code in enumerate(iata_codes)]
        for item in codes_and_ids:
            object_id, code = item
            endpoint = self.SHEETY_ENDPOINT + f"/{object_id}"
            iata_data = {
                "price": {
                    "iataCode": code,
                }
            }
            response = requests.put(endpoint, json=iata_data, headers=self.headers)
            response.raise_for_status()
