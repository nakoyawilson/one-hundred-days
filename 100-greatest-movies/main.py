from bs4 import BeautifulSoup
import requests
import json

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
greatest_movies = response.text

soup = BeautifulSoup(greatest_movies, "html.parser")
script_text = soup.find(name="script", id="__NEXT_DATA__").contents
data = json.loads(script_text[0])
movies = [data["props"]["pageProps"]["data"]["getArticleByFurl"]["_layout"][7]["content"]["images"][movie]["titleText"] for movie in range(100)]
print(movies)