import os
import requests
from datetime import datetime, timedelta


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.API_KEY = os.environ["KIWI_API_KEY"]
        self.SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
        self.headers = {
            "apikey": self.API_KEY,
        }

    def search_for_flights(self, sheet_data, departure_iata, from_date, to_date, num_stop_overs):
        departure = departure_iata
        start_date = from_date
        end_date = to_date
        for list_item in sheet_data["prices"]:
            fly_to_code = list_item["iataCode"]
            price_metric = list_item["lowestPrice"]
            query = {
                "fly_from": departure,
                "fly_to": fly_to_code,
                "date_from": start_date,
                "date_to": end_date,
                "vehicle_type": "aircraft",
                "max_stopovers": num_stop_overs,
                "curr": "GBP",
                "nights_in_dst_from": 4,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "selected_cabins": "M",
                "one_for_city": 1,
            }
            response = requests.get(self.SEARCH_ENDPOINT, headers=self.headers, params=query)
            response.raise_for_status()
            data = response.json()
            messages = []
            for item in data["data"]:
                flight_price = item["price"]
                if flight_price <= price_metric:
                    departure_city = item["cityFrom"]
                    departure_airport = item["flyFrom"]
                    arrival_city = item["cityTo"]
                    arrival_airport = item["flyTo"]
                    trip_length = item["nightsInDest"]
                    departure_date = item["route"][0]["local_departure"].split("T")
                    formatted_departure = departure_date[0]
                    date_to_use = datetime.strptime(formatted_departure, "%Y-%m-%d")
                    return_date = (date_to_use + timedelta(days=trip_length)).strftime("%Y-%m-%d")
                    google_flight_link = f"https://www.google.co.uk/flights?hl=en#flt={departure_airport}.{arrival_airport}.{formatted_departure}*{arrival_airport}.{departure_airport}.{return_date}"
                    if num_stop_overs == 0:
                        message = f"Low price alert! Only £{flight_price} to fly from {departure_city}-{departure_airport} to {arrival_city}-{arrival_airport}, from {formatted_departure} to {return_date}.\n{google_flight_link}"
                        messages.append(message)
                    elif num_stop_overs == 2:
                        via_city = item["route"][0]["cityTo"]
                        message = f"Low price alert! Only £{flight_price} to fly from {departure_city}-{departure_airport} to {arrival_city}-{arrival_airport}, from {formatted_departure} to {return_date}.\n\nFlight has 1 stop over, via {via_city}.\n{google_flight_link}"
                        messages.append(message)
            return messages
