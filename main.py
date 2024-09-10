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


top_tracks=sp.current_user_top_tracks(limit=50, offset=0, time_range='short_term') #top 50 recent tracks of the user
track_info=[]

for track in top_tracks['items']: #relevant info about tracks (id to join with features)
    track_info.append({
        'name':track['name'],
        'artist':track['artists'][0]['name'],
        'id':track['id']
    })

track_info_df=pd.DataFrame(track_info)

track_features=sp.audio_features([track['id'] for track in top_tracks['items']]) #audio features of the tracks
track_features_df=pd.DataFrame(track_features)

top_50_df=pd.merge(track_info_df, track_features_df, on='id') #both dataframes joined on id

print(top_50_df.columns)
print(top_50_df)





