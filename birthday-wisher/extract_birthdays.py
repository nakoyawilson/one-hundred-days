import re

with open("acnh_birthdays.txt") as data_file:
    birthdays = data_file.readlines()

for birthday_data in birthdays:
    birthday_regex = re.compile(r'(\d+) (\d+): (.*)')
    match_object = birthday_regex.search(birthday_data)
    name = match_object[3]
    month = match_object[1]
    day = match_object[2]
    data = f"{name},nwilsonautomated@yahoo.com,2001,{month},{day}\n"
    with open("birthdays.csv", "a") as csv_file:
        csv_file.write(data)