"""
This script is used to scrape lyrics from all of Kanye's songs using the Genius API.
"""

import os
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
                song = genius.search_song(song, 'Kanye West')
                song.save_lyrics(f"{song}_lyrics")
                
                # Move the saved lyrics to appropriate folder (in data/lyrics)
                os.rename(f"{song}_lyrics", f"data/lyrics/{song}_lyrics")
                break
            except:
                pass

        # Save lyrics
        #  Read in lyrics from JSON
        info = json.load(open(os.path.join(os.getcwd(), 'src', 'data', 'lyrics', f'lyrics/{song}_lyrics.json)', 'r')))
        lyrics = info['lyrics']

        # Save lyrics to separate file
        with open(f'data/lryics/{song}_lyrics.txt', 'w') as f:
            f.write(lyrics)
        
        # Save song, info, and lyrics to DB
        database.execute(f"INSERT INTO kanye VALUES ('{song}', '{album}', {0}, '{lyrics}')")
