import os
import requests

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_input = input("Which exercises did you do today? ")

query_data = {
    "query": user_input,
}

response = requests.post(exercise_endpoint, headers=headers, data=query_data)
print(response.text)