import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/gp/product/B0762LT49K/ref=ox_sc_saved_title_9?smid=A3686AOLDPXXOD&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers=headers)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")
price = soup.select_one("#priceblock_ourprice").getText()
print(price)
