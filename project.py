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
class Song:
    def __init__(self, artist, title, lyrics, songfile):
        self.artist = artist
        self.title = title
        self.lyrics = lyrics
        self.songfile = songfile
    











"""
    June
"""










"""
    Kumail: if main, and parse_args
"""
from argparse import ArgumentParser
import sys

#will be finished once we determine amount of arguments
def parse_args(args_list):
    parser = ArgumentParser()
    #parser.add_argument() - Need to add arguments
    return parser.parse_args(args_list)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    #call functions

"""
    Shalom: Input User Info Function
"""

