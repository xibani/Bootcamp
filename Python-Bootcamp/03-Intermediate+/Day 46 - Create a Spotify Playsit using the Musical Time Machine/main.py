from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + str(date))
soup = BeautifulSoup(response.text, "html.parser")
songs_link = soup.find_all(name="h3", class_="a-no-trucate")
songs_names = [song.getText(strip=True) for song in songs_link]
print(songs_names)

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="1ecf6c2d21ec4dfcbd887d104002c959",
        client_secret="cf5f5ea550a244d4b8e02bdbe730130e",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()['id']
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in songs_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)