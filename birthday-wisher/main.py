import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "example_email@gmail.com"
MY_PASSWORD = "ExamplePassword123"
EMAIL_PROVIDER = "smtp.gmail.com"

birthday_data = pandas.read_csv("birthdays.csv")

date_today = dt.datetime.now()
today_month = date_today.month
today_day = date_today.day

letter_templates = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

for row in birthday_data.itertuples(index=False, name="Person"):
    recipient_name = row.name
    recipient_email = row.email
    birthday_month = row.month
    birthday_day = row.day
    if birthday_month == today_month and birthday_day == today_day:
        letter_template = random.choice(letter_templates)
        with open(letter_template) as template:
            letter = template.read()
            email_message = letter.replace("[NAME]", recipient_name)
            with smtplib.SMTP(EMAIL_PROVIDER) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=recipient_email,
                                    msg=f"Subject: Happy Birthday, {recipient_name}!\n\n{email_message}")




