import os
import requests

SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
SHEETY_POST_ENDPOINT = os.environ["SHEETY_POST_ENDPOINT"]

print(
    "Welcome to Nakoya's Flight Club.\nWe find the best flight deals and email you."
)
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
emails_do_not_match = True
while emails_do_not_match:
    email = input("What is your email?\n")
    validate_email = input("Type your email again.\n")
    if email == validate_email:
        headers = {
            "Authorization": SHEETY_AUTH,
        }
        data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }
        response = requests.post(SHEETY_POST_ENDPOINT, json=data, headers=headers)
        response.raise_for_status()
        print("Success! Your email has been added.")
        emails_dont_match = False
    else:
        print("The emails entered don't match. Please try again.")
