import requests

parameters = {
    "lat": 10.707250,
    "lon": -61.554400,
    "appid": API_KEY,
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
# print(response.status_code)
weather_data = response.json()
print(weather_data)