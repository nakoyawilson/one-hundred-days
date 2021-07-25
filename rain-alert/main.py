import requests

parameters = {
    "lat": 10.707250,
    "lon": -61.554400,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_forecasts = [weather_data["hourly"][index]["weather"][0]["id"] for index, data_point in
                    enumerate(weather_data["hourly"]) if index < 12]
for condition_code in hourly_forecasts:
    if condition_code < 700:
        print("Bring an Umbrella")
        break