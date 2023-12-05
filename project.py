import os
from argparse import ArgumentParser
import sys
import json
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
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
    Jason: Song info class, spotify api + genius connection
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
    return lyrics










"""
    June: allows user input and checks if the song exists
"""
def get_spotify_song():
    # Set up your Spotify API credentials
    #client_id = 'client_id_#'
    #client_secret = 'client_secret_#'

    # Set up Spotify API client
    #sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    # Get user input for artist and song
    user_input = input("Enter artist name and song title separated by a comma (e.g., Artist Name, Song Title): ")

    # Split the user input into artist and song
    artist_name, song_title = map(str.strip, user_input.split(','))

    return artist_name, song_title

"""
    Shalom: Song playing GUI
"""
def play_song(song):
    lines = song.lyrics.split("\n")
    for line in lines:
        words = line.split(' ')
        for word in words:
            print('\x1b[6;30;42m' + word + '\x1b[0m')
            time.sleep(0.15)

def add_to_queue(song):
    pass

"""
    Kumail: if main, and parse_args
"""
def main():
    an, st = get_spotify_song()
    lyrics = spot_ap(an, st)
    songInfo = info(an, st, lyrics, "")
    play_song(songInfo)
    
    

"""
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("artist_name", type = str, help="Name of the artist who made the song")
    parser.add_argument("song_title", type =str, help="The title of the song")
    return parser.parse_args(arglist)
"""

if __name__ == "__main__":
    #args = parse_args(sys.argv[1:])
    main()

