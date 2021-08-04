from bs4 import BeautifulSoup
import requests

date = input("What date you would like to travel to? Type the date in the format YYYY-MM-DD: ")
url = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(url)
response.raise_for_status()
hot_100_data = response.text

soup = BeautifulSoup(hot_100_data, "html.parser")
# print(soup.prettify())
songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
artistes = soup.find_all(name="span", class_="chart-element__information__artist text--truncate color--secondary")
song_titles = [song.getText() for song in songs]
song_artistes = [artiste.getText() for artiste in artistes]
print(song_titles)
print(song_artistes)
