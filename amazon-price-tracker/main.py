import requests
from bs4 import BeautifulSoup
import smtplib
import os

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]
EMAIL_PROVIDER = "smtp.gmail.com"
RECIPIENT = os.environ["RECIPIENT"]
COMPARED_PRICE = 120

url = "https://www.amazon.com/gp/product/B0762LT49K/ref=ox_sc_saved_title_9?smid=A3686AOLDPXXOD&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers=headers)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")
price_as_string = soup.select_one("#priceblock_ourprice").getText()
price_as_float = float(price_as_string.replace("$", ""))
product_name = soup.select_one("#title").getText().strip()

if price_as_float < COMPARED_PRICE:
    with smtplib.SMTP(EMAIL_PROVIDER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECIPIENT,
                            msg=f"Subject: Amazon Price Alert!\n\n{product_name} is now {price_as_string}\n{url}")