import os
from argparse import ArgumentParser
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

    '''
    artist_name = current['item']['album']['artists'][0]['name']
    song_title = current['item']['name']
    '''
    song = genius.search_song(title=song_title, artist=artist_name)
    lyrics = song.lyrics
    print(lyrics)

"""
while True:
    current = spotify_object.currently_playing()
    status = current['currently_playing_type']
    
    if status == 'track':
        artist_name = current['item']['album']['artists'][0]['name']
        song_title = current['item']['name']
        length = current['item']['duration_ms']
        progress = current['progress_ms']
        time_left = int(((length-progress)/1000))
        
        song = genius.search_song(title=song_title, artist=artist_name)
        lyrics = song.lyrics
        print(lyrics)
        
        time.sleep(time_left)
        
    elif status == 'ad':
        time.sleep(30)
"""
"""
Client ID
59b86ae6790f4754949194665425d882
Client secret
8b25728b46ed4756b75698e8b71b4e88
Genius Access Token
Lpt-Wapnelbf2wGB7pGd_WEitsimXTYCtkNFE5NTB-dl451svFCQax4zmR1TV8qL
Spotify Access Token:
BQCELDO8mj0yJbK1Y36_Au9sFOnu2r-3JCAVDDgGHeJ3Z9zwBYDcLLxGvF2wvpySLr_1kNEYRijxTCxig7cjAnHHrh9f6pFnlfc7Km1oSd0rz5ypromzWAuz4xRWv5ugNvRSSVcGX_emwxiOqwwwxV0Zh1TPYalb2Yr_ReBwIks0Dh2ZLcMQxII
"""
""" uri https://google.com"""

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
    