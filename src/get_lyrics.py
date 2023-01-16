"""
This script is used to scrape lyrics from all of Kanye's songs using the Genius API.
"""

import os
import shutil
import json
import sqlite3
from lyricsgenius import Genius

genius = Genius(access_token=os.environ['GENIUS_ACCESS_TOKEN'])

# Database config
connector = sqlite3.connect(os.path.join(os.getcwd(), 'src', 'data', 'lyrics.db'))
database = connector.cursor()

# Song generation
song_info = json.load(open(os.path.join(os.getcwd(), 'src', 'data', 'kanye_songs.json'), 'r'))

for album, songs in song_info.items():
    # Iterate through songs and get lyrics
    for song in songs:
        while True: # Genius's API sometimes returns error for taking too long
            try:
                # Get current song
                fetch_song = genius.search_song(song, 'Kanye West')
                
                # Save song
                filename = f"{song}_lyrics.json".replace(' ', '_').lower()
                fetch_song.save_lyrics(filename)
                shutil.move(
                    os.path.join(os.getcwd(), filename),
                    os.path.join(os.getcwd(), 'src', 'data', 'lyrics', filename)
                )
                break
            except:
                pass
