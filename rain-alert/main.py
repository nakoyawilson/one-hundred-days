import requests
from twilio.rest import Client
import os

api_key = os.environ["OWM_API_KEY"]
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
from_phone_num = os.environ["FROM_PHONE_NUMBER"]
to_phone_num = os.environ["TO_PHONE_NUMBER"]

parameters = {
    "lat": 10.707250,
    "lon": -61.554400,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_forecasts = [weather_data["hourly"][index]["weather"][0]["id"] for index, data_point in
                    enumerate(weather_data["hourly"]) if index < 12]
for condition_code in hourly_forecasts:
    if condition_code < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="It's going to rain today. Remember to bring an ☔️",
            from_= from_phone_num,
            to= to_phone_num
        )
        print(message.status)
        break