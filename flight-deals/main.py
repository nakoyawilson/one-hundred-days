from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

DEPARTURE_LIST = ["London"]

data_manager = DataManager()
flight_data = FlightData()
notification_manager = NotificationManager()
flight_search = FlightSearch()

# # Get list of cities
# cities = data_manager.city_list
#
# # Get list of IATA codes
# city_codes = flight_data.find_iata_codes(city_names=cities)
#
# # Add IATA codes to Google Sheet
# data_manager.add_iata_code(iata_codes=city_codes)

# Get updated Google Sheet data
updated_data = data_manager.get_data()

# Get departure location IATA code
departure_location = flight_data.find_iata_codes(city_names=DEPARTURE_LIST)
departure_code = departure_location[0]

# Use updated data to search for flights
tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
six_months_later = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")
stop_overs = 0
cheap_flights = flight_search.search_for_flights(sheet_data=updated_data, departure_iata=departure_code, from_date=tomorrow,
                                           to_date=six_months_later, num_stop_overs=stop_overs)

if len(cheap_flights) == 0:
    stop_overs = 2
    cheap_flights = flight_search.search_for_flights(sheet_data=updated_data, departure_iata=departure_code,
                                                     from_date=tomorrow,
                                                     to_date=six_months_later, num_stop_overs=stop_overs)

for cheap_flight in cheap_flights:
    notification_manager.send_sms(sms_body=cheap_flight)
    email_contents = f"Subject: New Low Price Flight!\n\n{cheap_flight}"
    notification_manager.send_emails(email_contents)