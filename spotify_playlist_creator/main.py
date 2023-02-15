from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"
DATE = input("Which DATE do you want to travel to? Type the date in this format YYYY-MM-DD: ")
CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT = "https://example.com"



res = requests.get(f"{URL}{DATE}/")
html = res.text


soup = BeautifulSoup(html, "html.parser")
data = soup.select(selector="li h3")
songs = [song.getText().strip("\n\t") for song in data[:100]]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET, 
    redirect_uri=REDIRECT, 
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="spotify_playlist_creator/token.txt"
    ))

user_id = sp.current_user()["id"]
new_playlist = sp.user_playlist_create(user_id, name=f"{DATE} Billboard 100", public=False, description=f"Top 100 songs from {DATE}")["id"]

track_uri = []

for song in songs:
    results = sp.search(q=f"track:{song}, year:{DATE[:4]}", limit=1)

    for idx, track in enumerate(results['tracks']['items']):
        track_uri.append(track["uri"])

sp.user_playlist_add_tracks(user_id, new_playlist, track_uri)




