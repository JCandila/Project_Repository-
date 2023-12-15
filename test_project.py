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
import ssl

from project import spot_api
from project import get_spotify_song
import unittest

class TestSA(unittest.TestCase):
    def test_results(self):
        #Testing the results of songs not make sure nothing returns as None
        self.assertIsNotNone(spot_api("DEVO", "Fresh"))
        self.assertIsNotNone(spot_api("DragonForce", "Through the fire and flames"))
        self.assertIsNotNone(spot_api("Saliva", "Click Click Boom"))


    def test_values(self):
        #Testing the raised errors that occur if bad inputs are made
        self.assertRaises(IndexError, spot_api, "9r3902r", "3489fe2h")
        self.assertRaises(ValueError, spot_api, "hehethis should fail", "momoooooo")

    
    def test_get_spotify_song(self):
        """
        This test file checks if the function correctly extracts the artist name and song title from valid input.
        """      
        # Test with valid input
        user_input = "Cutting Crew, (I Just) Died In Your Arms"
        with unittest.mock.patch('builtins.input', return_value=user_input):
            artist, title = get_spotify_song()

        assert artist == "Cutting Crew"
        assert title == "(I Just) Died In Your Arms"
        
        
