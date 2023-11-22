import os
from argparse import ArgumentParser
import sys
import json
import time
import spotipy
import lyricsgenius as lg
"""
    Project code of the Spotify Karaoke
    Jason Candila, Kumail Jafari, June Lee, Shalom Akpakla
"""
"""
Class: Song()
    def _init_(artist, title, lyrics, songfile)

"""
"""
    Jason
"""
class info:
    def __init__(self, artist, title, lyrics, songfile):
        self.artist = artist
        self.title = title
        self.lyrics = lyrics
        self.songfile = songfile
    
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
    June
"""










"""
    Kumail: if main, and parse_args
"""
def main(an, st):
    song_info = info(an, st, "", "")
    
    print(spot_ap(song_info.artist, song_info.title))
    


def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("artist_name", type = str, help="Name of the artist who made the song")
    parser.add_argument("song_title", type =str, help="The title of the song")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.artist_name, args.song_title)

"""
    Shalom: Input User Info Function
"""

