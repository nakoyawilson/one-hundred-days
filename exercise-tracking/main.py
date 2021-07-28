import os
import requests
from datetime import datetime
import json

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_AUTH = os.environ["SHEETY_AUTH"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

user_input = input("Which exercises did you do today? ")

query_data = {
    "query": user_input,
}

query_json_data = json.dumps(query_data)

nutritionix_response = requests.post(exercise_endpoint, headers=headers, data=query_json_data)
exercise_data = nutritionix_response.json()

today = datetime.now()
current_date = today.strftime("%d/%m/%Y")
current_time = today.strftime("%H:%M:%S %p")

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": SHEETY_AUTH,
}

for exercise in exercise_data["exercises"]:
    exercise_name = exercise["name"]
    exercise_duration = exercise["duration_min"]
    calories_burned = exercise["nf_calories"]
    sheety_data = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise_name.title(),
            "duration": round(exercise_duration),
            "calories": round(calories_burned),
        }
    }
    sheety_json_data = json.dumps(sheety_data)
    sheety_response = requests.post(SHEETY_ENDPOINT, data=sheety_json_data, headers=sheety_headers)