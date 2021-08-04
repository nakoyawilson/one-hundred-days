from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
REDIRECT_URI = "http://example.com"

date = input("What date you would like to travel to? Type the date in the format YYYY-MM-DD: ")
url = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(url)
response.raise_for_status()
hot_100_data = response.text

soup = BeautifulSoup(hot_100_data, "html.parser")
songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
artists = soup.find_all(name="span", class_="chart-element__information__artist text--truncate color--secondary")
song_titles = [song.getText() for song in songs]
song_artists = [artist.getText() for artist in artists]
print(song_titles)
print(song_artists)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private"))
user_id = sp.current_user()["id"]