import requests
import os

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

post_pixel_data = {
    "date": "20210727",
    "quantity": "50",
}

# Post a pixel
response = requests.post(url=post_pixel_endpoint, json=post_pixel_data, headers=headers)
print(response.text)