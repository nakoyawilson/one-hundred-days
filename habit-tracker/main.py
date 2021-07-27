import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

#  Create a user
create_new_user = input("Would you like to create a new user? Type 'y' or 'n': ")
if create_new_user.lower() == 'y':
    pixela_token = input("Enter a token. Validation rule: [ -~]{8,128}: ")
    pixela_username = input("Enter a username. Validation rule: [a-z][a-z0-9-]{1,32}: ")
    user_params = {
        "token": pixela_token,
        "username": pixela_username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)

# Create a graph
graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"
headers = {
    "X-USER-TOKEN": pixela_token,
}
create_new_graph = input("Would you like to create a new graph? Type 'y' or 'n': ")
if create_new_graph.lower() == 'y':
    pixela_username = input("Enter your username: ")
    pixela_token = input("Enter your token: ")
    graph_id = input("Enter a graph id. Validation rule: ^[a-z][a-z0-9-]{1,16}: ")
    graph_name = input("Enter a name for your graph: ")
    graph_units = input("Enter the unit of measurement: ")
    unit_type = input("Enter the unit type. Type 'int' or 'float'): ")
    colour = input("Choose a color: 'shibafu', 'momiji', 'sora', 'ichou', 'ajisai' or 'kuro': ")
    graph_config = {
        "id": graph_id,
        "name": graph_name,
        "unit": graph_units,
        "type": unit_type,
        "color": colour,
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)

# Post a pixel
post_pixel_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{graph_id}"

post_a_pixel = input("Would you like to post a new pixel? Type 'y' or 'n': ")
if post_a_pixel.lower() == 'y':
    pixela_username = input("Enter your username: ")
    pixela_token = input("Enter your token: ")
    use_today = input("Do you want to use today's date? Type 'y' or 'n': ")
    if use_today.lower() == 'y':
        today = datetime.now()
        formatted_date = today.strftime("%Y%m%d")
    elif use_today == 'n':
        formatted_date = input("Enter the date in the form YYYYMMDD: ")
    amount_of_activity = input("Enter the amount of activity completed: ")
    pixel_data = {
        "date": formatted_date,
        "quantity": amount_of_activity,
    }
    response = requests.post(url=post_pixel_endpoint, json=pixel_data, headers=headers)
    print(response.text)

# Update a pixel
update_a_pixel = input("Would you like to update a pixel? Type 'y' or 'n': ")
if update_a_pixel.lower() == 'y':
    pixela_username = input("Enter your username: ")
    pixela_token = input("Enter your token: ")
    date_to_update = input("Enter the date to update in the form YYYYMMDD: ")
    updated_activity = input("What is the updated amount of activity? ")
    update_pixel_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{graph_id}/{date_to_update}"
    new_pixel_data = {
        "quantity": updated_activity,
    }
    response = requests.put(url=update_pixel_endpoint, json=new_pixel_data, headers=headers)
    print(response.text)

# Delete a pixel
delete_a_pixel = input("Would you like to delete a pixel? Type 'y' or 'n': ")
if delete_a_pixel.lower() == 'y':
    pixela_username = input("Enter your username: ")
    pixela_token = input("Enter your token: ")
    date_to_delete = input("Enter the date to delete in the form YYYYMMDD: ")
    delete_pixel_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{graph_id}/{date_to_delete}"
    response = requests.delete(url=delete_pixel_endpoint, headers=headers)
    print(response.text)
