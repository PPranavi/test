from flask import Flask, render_template
import os
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

@app.route('/')

def hello_world():
    reference = ["Shawn Mendes", "BLACKPINK", "Panic! At The Disco", "Dua Lipa", "Zedd"]
    artists_id = ["7n2wHs1TKAczGzO7Dd2rGr", "41MozSoPIsD1dJM0CLPjZF", "20JZFwl6HVl6yg8a4H3ZqK", "6M2wZ9GZgrQXHCFfjv46we", "2qxJFvFYMEDqd7ui6kSAcq"]
    
    random_number = random.randint(0,4) 
    artist_name = reference[random_number]
    artist_img = spotify.search(q='artist:' + artist_name, type='artist')['artists']['items'][0]['images'][0]['url']
    artist_id = artists_id[random_number]
    artist_top_10 = spotify.artist_top_tracks(artist_id, country="US")
    tracks = []
    tracks_preview_url = []
    tracks_album_img = []
    for i in range(10):
        tracks.append(artist_top_10["tracks"][i]["name"])
        tracks_preview_url.append(artist_top_10["tracks"][i]["preview_url"])
        tracks_album_img.append(artist_top_10["tracks"][i]["album"]["images"][0]["url"])
    random_track = random.randint(0,9) 

    
    return render_template(
        "index.html",
        name = artist_name,
        image = artist_img,
        tracks = tracks,
        len = len(tracks),
        track_name = tracks[random_track],
        preview = tracks_preview_url[random_track],
        track_image = tracks_album_img[random_track]
    )
    
app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP', '0.0.0.0'),
    debug = True
)