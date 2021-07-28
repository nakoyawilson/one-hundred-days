import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
from_phone_num = os.environ["FROM_PHONE_NUMBER"]
to_phone_num = os.environ["TO_PHONE_NUMBER"]


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    pass