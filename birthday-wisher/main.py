##################### Extra Hard Starting Project ######################

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import random

birthday_data = pandas.read_csv("birthdays.csv")

date_today = dt.datetime.now()
today_month = date_today.month
today_day = date_today.day

letter_templates = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

for row in birthday_data.itertuples(index=False, name="Person"):
    name = row.name
    email = row.email
    birthday_month = row.month
    birthday_day = row.day
    if birthday_month == today_month and birthday_day == today_day:
        letter_template = random.choice(letter_templates)
        with open(letter_template) as template:
            letter = template.read()
            email_message = letter.replace("[NAME]", name)
            print(email_message)




