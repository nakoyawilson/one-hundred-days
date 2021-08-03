from bs4 import BeautifulSoup
import requests
import json
import re

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
greatest_movies = response.text

soup = BeautifulSoup(greatest_movies, "html.parser")
script_text = soup.find(name="script", id="__NEXT_DATA__").contents
data = json.loads(script_text[0])
movies = [data["props"]["pageProps"]["data"]["getArticleByFurl"]["_layout"][7]["content"]["images"][movie]["titleText"] for movie in range(100)]
movies.reverse()

# Correctly format and number list
new_list = []
for movie in movies:
    pattern = r'\d+\) '
    if re.search(pattern, movie):
        new_list.append(re.sub(pattern, "", movie))
    else:
        new_list.append(movie)

with open("movies.txt", "w") as file:
    count = 1
    for movie in new_list:
        file.write(f"{count}) {movie}\n")
        count += 1
