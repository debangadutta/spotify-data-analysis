import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import json
from datetime import datetime
import s3fs

client_ID = "c35b9b1e024941e7a1fa9a29815f6e10"
client_secret = "89db980930da4a47928a14ce645eca8e"

#Spotify Authentication
auth = SpotifyClientCredentials(client_id=client_ID, client_secret = client_secret)

sp = spotipy.Spotify(client_credentials_manager = auth)

songs = sp.album_tracks(
    album_id="https://open.spotify.com/album/6PFPjumGRpZnBzqnDci6qJ?si=vRd6OYWuQXKFAObEJU9GMA",
    )

print(songs)