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

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Don't Break the Chain",
    "unit": "minutes",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": pixela_token,
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)