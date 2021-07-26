import requests
import os
from datetime import datetime, timedelta

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
    "q": COMPANY_NAME,
}


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

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
av_response = requests.get("https://www.alphavantage.co/query", params=alpha_vantage_params)
av_response.raise_for_status()
stock_data = av_response.json()
yesterday_price = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
day_before_price = float(stock_data["Time Series (Daily)"][day_before]["4. close"])
price_difference = yesterday_price - day_before_price
percentage = price_difference/yesterday_price * 100
if percentage >= 5 or percentage <= -5:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    top_3_articles = [news_data["articles"][article] for article in range(3)]
else:
    print("Insignificant change in price")


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

