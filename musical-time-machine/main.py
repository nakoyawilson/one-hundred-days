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
artists_list = [artist.getText() for artist in artists]
song_artists = []
for artist in artists_list:
    if "Featuring" in artist:
        new_artist = artist.replace("Featuring ", "")
        song_artists.append(new_artist)
    elif "With" in artist:
        new_artist = artist.replace("With ", "")
        song_artists.append(new_artist)
    else:
        song_artists.append(artist)

songs_and_artists = list(zip(song_titles, song_artists))

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private"))

search_queries = [f"{artist} {song}" for song, artist in songs_and_artists]
results = []
for query in search_queries:
    try:
        result = sp.search(q=query, limit=1)["tracks"]["items"][0]["uri"]
    except IndexError:
        continue
    else:
        results.append(result)
print(f"{len(results)} songs successfully added to playlist")

user_id = sp.current_user()["id"]
name = f"{date} Billboard 100"
public = False
description = "Billboard top 100 music from date in the past"
playlist = sp.user_playlist_create(user=user_id, name=name, public=public, description=description)
playlist_id = playlist["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=results, position=None)