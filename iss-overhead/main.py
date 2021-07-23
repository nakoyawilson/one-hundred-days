import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 10.597344
MY_LONG = -61.339448
MY_EMAIL = "example_email@gmail.com"
MY_PASSWORD = "ExamplePassword123"
EMAIL_PROVIDER = "smtp.gmail.com"
RECIPIENT = "example_email@gmail.com"


# Your position is within +5 or -5 degrees of the ISS position.
def within_five_degrees():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_now_data = response.json()

    iss_latitude = float(iss_now_data["iss_position"]["latitude"])
    iss_longitude = float(iss_now_data["iss_position"]["longitude"])

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.utcnow()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


def send_email():
    with smtplib.SMTP(EMAIL_PROVIDER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECIPIENT,
                            msg="Subject: Look up!\n\nThe ISS is close. Go outside and look up!")


while True:
    time.sleep(60)
    if within_five_degrees() and is_dark():
        send_email()
