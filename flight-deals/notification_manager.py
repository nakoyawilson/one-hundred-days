import os
from twilio.rest import Client
import smtplib
import requests

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
        self.AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
        self.FROM_PHONE_NUMBER = os.environ["FROM_PHONE_NUMBER"]
        self.TO_PHONE_NUMBER = os.environ["TO_PHONE_NUMBER"]
        self.FROM_EMAIL = os.environ["FROM_EMAIL"]
        self.FROM_EMAIL_PASSWORD = os.environ["FROM_EMAIL_PASSWORD"]
        self.EMAIL_PROVIDER = "smtp.gmail.com"
        self.SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
        self.headers = {
            "Authorization": self.SHEETY_TOKEN,
        }
        self.USERS_ENDPOINT = os.environ["USERS_ENDPOINT"]


    def send_sms(self, sms_body):
        client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)
        message = client.messages \
            .create(
            body= sms_body,
            from_= self.FROM_PHONE_NUMBER,
            to= self.TO_PHONE_NUMBER,
        )
        print(message.status)

    def send_emails(self, email_body):
        response = requests.get(self.USERS_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        user_data = response.json()
        recipients = [list_item["email"] for list_item in user_data["users"]]
        with smtplib.SMTP(self.EMAIL_PROVIDER) as connection:
            connection.starttls()
            connection.login(user=self.FROM_EMAIL, password=self.FROM_EMAIL_PASSWORD)
            connection.sendmail(from_addr=self.FROM_EMAIL, to_addrs=recipients,
                                msg=email_body.encode('utf-8'))


