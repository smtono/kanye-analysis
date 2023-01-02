"""
This script is used to scrape lyrics from all of Kanye's songs using the Genius API.
"""

import os
from lyricsgenius import Genius

genius = Genius(access_token=os.environ['GENIUS_ACCESS_TOKEN'])

# Get lyrics for all Kanye songs
while True:
    try:
        #artist = genius.search_artist('Kanye West')
        #artist.save_lyrics("kanye_lyrics")
        song = genius.search_song('Through the Wire', 'Kanye West')
        song.save_lyrics()
        break
    except:
        pass

# Read in lyrics from JSON
