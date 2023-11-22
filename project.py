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
    June: allows user input and checks if the song exists
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_spotify_song():
    # Set up your Spotify API credentials
    client_id = 'client_id_#'
    client_secret = 'client_secret_#'

    # Set up Spotify API client
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    # Get user input for artist and song
    user_input = input("Enter artist name and song title separated by a comma (e.g., Artist Name, Song Title): ")

    # Split the user input into artist and song
    artist_name, song_title = map(str.strip, user_input.split(','))

    # Use Spotify API to search for the song
    results = sp.search(q=f"artist:{artist_name} track:{song_title}", type='track')

    # Check if the user inputted song exists
    if results['tracks']['items']:
        # Get the first result (assuming it's the most relevant)
        first_result = results['tracks']['items'][0]

        # Extract relevant information
        song_name = first_result['name']
        artist_name = first_result['artists'][0]['name']
        album_name = first_result['album']['name']
        spotify_url = first_result['external_urls']['spotify']

        # Print the information
        print(f"\nSong: {song_name}\nArtist: {artist_name}\nAlbum: {album_name}\nSpotify URL: {spotify_url}")

    else:
        print("No results found for the inputted artist and song title.")

# Call the function
get_spotify_song()









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
def play_song(song):
    lines = song.lyrics.split("\n")
    for line in lines:
        words = line.split(' ')
        for word in words:
            print('\x1b[6;30;42m' + word + '\x1b[0m')
            time.sleep(0.15)

def add_to_queue(song):
    pass
