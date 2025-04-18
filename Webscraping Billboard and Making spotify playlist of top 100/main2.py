from bs4 import BeautifulSoup
import lxml
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()
import os


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
URL = "https://www.billboard.com/charts/hot-100/"

response = requests.get(url=URL, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
sp = spotipy.Spotify(
    auth_manager= SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://spotify.com",
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt",
        username=os.getenv("USERNAME")
    )
)
user_id = sp.current_user()['id']
year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
song_uris = []
year = year.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{year} BillBoard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
