import requests
import os
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
pixela_token = os.environ["PIXELA_TOKEN"]
pixela_username = os.environ["PIXELA_USERNAME"]

user_params = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # Create the user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"

graph_id = "graph1"

graph_config = {
    "id": graph_id,
    "name": "Don't Break the Chain",
    "unit": "minutes",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": pixela_token,
}

# # Create the graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{graph_id}"

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")
minutes_of_activity = input("How many minutes did you spend on the activity today? ")

pixel_data = {
    "date": formatted_date,
    "quantity": minutes_of_activity,
}

# # Post a pixel
# response = requests.post(url=post_pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{graph_id}/{formatted_date}"

updated_minutes = input("What is the updated number of minutes? ")

new_pixel_data = {
    "quantity": updated_minutes,
}

# # Update a pixel
# response = requests.put(url=update_pixel_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{graph_id}/{formatted_date}"

# # Delete a pixel
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)