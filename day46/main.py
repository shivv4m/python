import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()
import os

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
uris = [sp.search(title)['tracks']['items'][0]['uri'] for ]




