import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import json
from datetime import datetime
import s3fs

client_ID = "c35b9b1e024941e7a1fa9a29815f6e10"
client_secret = ""

#Spotify Authentication
auth = SpotifyClientCredentials(client_id=client_ID, client_secret = client_secret)

sp = spotipy.Spotify(client_credentials_manager = auth)

results = sp.album_tracks(
    album_id="https://open.spotify.com/album/6PFPjumGRpZnBzqnDci6qJ?si=huhS-psmTUiIkhaS7Eed6g"
    )

songs = results['items']

while results['next']:
    results = sp.next(results)
    songs.extend(results['items'])

song_list = []

for song in songs:
    refined_song = {
        'track_number' : song['track_number'],
        'name' : song['name'],
        "duration_mins" : round(song['duration_ms']/60000, 2)
    }
    song_list.append(refined_song)

df = pd.DataFrame(song_list)
df.to_csv("linkin_park_album_songs.csv")