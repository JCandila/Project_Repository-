import os
import base64
from argparse import ArgumentParser
from requests import post, get
import sys
import json
import time
import spotipy
import lyricsgenius as lg
import io
if sys.version_info < (3, 0):
    from urllib2 import urlopen
else:
    from urllib.request import urlopen
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius as lg
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import colorthief as ct
from PIL import ImageTk, Image
from colorthief import ColorThief
import math
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
    def __init__(self, artist, title, lyrics, image, duration):
        self.artist = artist
        self.title = title
        self.lyrics = lyrics
        self.image = image
        self.duration = duration
    
    
def gui_info(lyrics, image, duration):
    #raw_lyrics = open("/Users/shalomakpakla/Documents/INST326_exercises/heartless.txt", "r")
    song = lyrics.split("\n")
    total_lines = len(song)
    fd = urlopen(image)
    file_path = io.BytesIO(fd.read())
    color_thief = ColorThief(file_path)
    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)
    #convert rgb to hex
    def rgb_to_hex(r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    background_fill =(rgb_to_hex(dominant_color[0],dominant_color[1],dominant_color[2]))
    refresh_rate = int(math.floor(duration/(len(song)/2))) 
    return song, total_lines, background_fill, refresh_rate, file_path
    
class Karaoke(tk.Tk):
    line = 0
    def __init__(self, song, duration, total_lines, background_fill, refresh_rate, file_path):
        super().__init__()
        self.song = song
        self.refresh_rate = refresh_rate
        self.total_lines = total_lines
        
        # configure the root window
        self.title('Karoake')
        self.resizable(True, True)
        self.geometry('1500x750')
        self['bg'] = f'{background_fill}'

        #album art
        img = Image.open(file_path) 
        img = img.resize((350,350)) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.place(x=30,y=375)
        picture.image = img
        picture.pack()
        
        #progress bar
        bar = Progressbar(self, orient = HORIZONTAL, length = 700, maximum = duration)
        bar.place(x=400, y=700)
        bar.pack(pady = 10)
        bar.step(1)
        bar.start(1000)
       
        # change the background color to black
        self.style = ttk.Style(self)
        self.style.configure(
            'TLabel',
            background='black',
            foreground='white')

        # Lyrics text
        self.label = ttk.Label(
            self,
            background = "black",
            text = self.song_line(),
            font=('futura', 40))
        self.label.pack(expand=True)

        # schedule an update for text every 6 second
        self.label.after(refresh_rate, self.update)
    
    def song_line(self):
        if self.line < self.total_lines or self.line %2 == 0 and self.line == self.total_lines:
            self.line += 2
            two_bar = ""
            #return song[self.line - 2 : self.line]
            for bar in self.song[self.line - 2 : self.line]:
                two_bar += bar + '\n'
            return two_bar
        if self.line != "\n" and self.line == self.total_lines:
                return self.song[self.line-2]
    
    def update(self):
        """ update the label every 6 seconds """

        self.label.configure(text=self.song_line())

        # schedule another timer
        self.label.after(self.refresh_rate, self.update)
        

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

    image = json_result["tracks"]["items"][0]["album"]["images"][1]["url"]
    duration = json_result["tracks"]["items"][0]["duration_ms"]
    
    song = genius.search_song(title=song_title, artist=artist_name)
    lyrics = song.lyrics
    
    
    return lyrics, image, duration

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
    Kumail: if main, and parse_args
"""
def main():
    an, st = get_spotify_song()
    lyrics, image, duration = spot_ap(an, st)
    songInfo = info(an, st, lyrics, image, duration)
    song, total_lines, background_fill, refresh_rate, file_path = gui_info(songInfo.lyrics, songInfo.image, songInfo.duration)
    print("A new Karaoke tab has opened")
    GUI = Karaoke(song, songInfo.duration, total_lines, background_fill, refresh_rate, file_path)
    GUI.mainloop()
   
    

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
    
