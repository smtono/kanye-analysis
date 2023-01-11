"""
This script is used to scrape lyrics from all of Kanye's songs using the Genius API.
"""

import os
import json
from lyricsgenius import Genius

songs = []
json.load(open('data/kanye_songs.json', 'r'))

genius = Genius(access_token=os.environ['GENIUS_ACCESS_TOKEN'])

# TODO: iterate through songs and get lyrics
# Get lyrics for all Kanye songs
for song in songs:
    while True:
        try:
            # TODO: change to current song
            song = genius.search_song(song, 'Kanye West')
            song.save_lyrics(f"{song}_lyrics")
            
            # TODO: Move the saved lyrics to appropriate folder (in data/lyrics)
            
            break
        except:
            pass

# TODO: Read in lyrics from JSON

# TODO: Save lyrics to separate file
