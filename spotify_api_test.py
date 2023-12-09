import os
import base64
from argparse import ArgumentParser
from requests import post, get
import sys
import json
import time
import spotipy
import lyricsgenius as lg

class info():
    def __init__(self, name, title):
        self.name = name
        self.title = title

def spot_ap(artist_name, song_title):
    os.environ['SPOTIPY_CLIENT_ID'] = "59b86ae6790f4754949194665425d882"
    os.environ['SPOTIPY_CLIENT_SECRET'] = "8b25728b46ed4756b75698e8b71b4e88"
    os.environ['SPOTIPY_REDIRECT_URI'] = "https://google.com"
    os.environ['GENIUS_ACCESS_TOKEN'] = "Lpt-Wapnelbf2wGB7pGd_WEitsimXTYCtkNFE5NTB-dl451svFCQax4zmR1TV8qL"

    spotify_client_id = os.environ.get('SPOTIPY_CLIENT_ID')
    spotify_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
    spotify_redirect_uri = os.environ.get('SPOTIPY_REDIRECT_URI')
    genius_access_token = os.environ.get('GENIUS_ACCESS_TOKEN')

    scopes = 'user-read-currently-playing'

    oauth_object = spotipy.SpotifyOAuth(client_id=spotify_client_id,
                                        client_secret=spotify_secret,
                                        redirect_uri=spotify_redirect_uri,
                                        scope=scopes)

    print(oauth_object)

    token_dict = oauth_object.get_access_token()
    token = token_dict['access_token']

    spotify_object = spotipy.Spotify(auth=token)


    genius = lg.Genius(genius_access_token)

    current = spotify_object.currently_playing()
    print(json.dumps(current, sort_keys=False, indent=4))

    auth_header = {"Authorization": "Bearer " + token}
    
    
    
    url = "https://api.spotify.com/v1/search"
    query = f"?q={artist_name, song_title}&type=artist,track&limit=1"
    
    query_url = url + query
    result = get(query_url, headers=auth_header)  
    json_result = json.loads(result.content)
    print(json.dumps(json_result, sort_keys=False, indent=5))
    
    image = json_result["tracks"]["items"][0]["album"]["images"][1]["url"]
    duration = json_result["tracks"]["items"][0]["duration_ms"]
    
    print(f"{image}")
    print(f"{duration}")
    
    song = genius.search_song(title=song_title, artist=artist_name)
    lyrics = song.lyrics


def main(an, st):
    song_info = info(an, st)
    
    print(spot_ap(song_info.name, song_info.title))
    


def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("artist_name", type = str, help="Name of the artist who made the song")
    parser.add_argument("song_title", type =str, help="The title of the song")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.artist_name, args.song_title)
    