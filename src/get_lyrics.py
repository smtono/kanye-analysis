"""
This script is used to scrape lyrics from all of Kanye's songs using the Genius API.
"""

import os
import json
import sqlite3
from lyricsgenius import Genius

# Database config
connector = sqlite3.connect(os.path.join(os.getcwd(), 'src', 'data', 'lyrics.db'))
database = connector.cursor()

# Song generation
songs = []
json.load(open('data/kanye_songs.json', 'r'))

genius = Genius(access_token=os.environ['GENIUS_ACCESS_TOKEN'])

# Iterate through songs and get lyrics
for song in songs:
    while True:
        try:
            # Get current song
            song = genius.search_song(song, 'Kanye West')
            song.save_lyrics(f"{song}_lyrics")
            
            # Move the saved lyrics to appropriate folder (in data/lyrics)
            os.rename(f"{song}_lyrics", f"data/lyrics/{song}_lyrics")
            
            break
        except:
            pass

# Save lyrics
# TODO: Read in lyrics from JSON

# TODO: Save lyrics to separate file
