import os
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
        self.AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
        self.FROM_PHONE_NUMBER = os.environ["FROM_PHONE_NUMBER"]
        self.TO_PHONE_NUMBER = os.environ["TO_PHONE_NUMBER"]

    def send_sms(self, sms_body):
        client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)
        message = client.messages \
            .create(
            body= sms_body,
            from_= self.FROM_PHONE_NUMBER,
            to= self.TO_PHONE_NUMBER,
        )
        print(message.status)