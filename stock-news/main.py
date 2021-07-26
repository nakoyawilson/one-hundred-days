import requests
import os
from datetime import datetime, timedelta
from twilio.rest import Client
from html.parser import HTMLParser

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

alpha_vantage_api_key = os.environ["AV_API_KEY"]
alpha_vantage_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": alpha_vantage_api_key,
}

news_api_key = os.environ["NEWS_API_KEY"]
news_params = {
    "apiKey": news_api_key,
    "qInTitle": COMPANY_NAME,
}

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
from_phone_num = os.environ["FROM_PHONE_NUMBER"]
to_phone_num = os.environ["TO_PHONE_NUMBER"]


class HTMLFilter(HTMLParser):
    text = ""

    def handle_data(self, data):
        self.text += data


def get_yesterday(num_days):
    date_today = datetime.now()
    delta = timedelta(days=num_days)
    return date_today - delta


def get_day_before_yesterday(date_yesterday, num_days):
    delta = timedelta(days=num_days)
    return date_yesterday - delta


# Get yesterday's date
if datetime.now().weekday() == 0:
    yesterday = get_yesterday(3)
elif datetime.now().weekday() == 6:
    yesterday = get_yesterday(2)
else:
    yesterday = get_yesterday(1)
# Get day before yesterday's date
if yesterday.weekday() == 0:
    day_before = get_day_before_yesterday(yesterday, 3)
else:
    day_before = get_day_before_yesterday(yesterday, 1)
yesterday = str(yesterday.date())
day_before = str(day_before.date())

# When STOCK price increases/decreases by 5% between yesterday and the day before yesterday,
# then get the first 3 news pieces for the COMPANY_NAME.
av_response = requests.get("https://www.alphavantage.co/query", params=alpha_vantage_params)
av_response.raise_for_status()
stock_data = av_response.json()
yesterday_price = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
day_before_price = float(stock_data["Time Series (Daily)"][day_before]["4. close"])
price_difference = yesterday_price - day_before_price
percentage = price_difference / yesterday_price * 100
if percentage >= 5 or percentage <= -5:
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    top_3_articles = [news_data["articles"][article] for article in range(3)]
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    for article in top_3_articles:
        if percentage > 0:
            subject = f"{STOCK}:️ 🔺{abs(int(percentage))}%"
        elif percentage < 0:
            subject = f"{STOCK}: 🔻{abs(int(percentage))}%"
        headline = f"Headline: {article['title']}"
        brief = f"Brief: {article['description']}"
        remove_html = HTMLFilter()
        remove_html.feed(brief)
        brief = remove_html.text
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"{subject}\n{headline}\n{brief}",
            from_=from_phone_num,
            to=to_phone_num
        )
        print(message.status)
