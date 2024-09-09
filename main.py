#load all the data from apis
#use spotipy

from dotenv import load_dotenv
import spotipy
import spotipy.oauth2 as oauth2
import pandas as pd
import os


load_dotenv()

client_id=os.getenv("CLIENT_ID")
client_secret=os.getenv("CLIENT_SECRET")
redirect_uri='http://localhost:5000/callback'


sp=spotipy.Spotify(
    auth_manager=spotipy.SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="user-top-read"
    )
)

top_tracks=sp.current_user_top_tracks(limit=50, offset=0, time_range='short_term')
track_names=[track['name'] for track in top_tracks['items']]
print(track_names)

