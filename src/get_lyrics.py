"""
This script is used to scrape lyrics from all of Kanye's songs using the Genius API.
"""

import os
from lyricsgenius import Genius

genius = Genius(access_token=os.environ['GENIUS_ACCESS_TOKEN'])

artist = genius.search_artist('Kanye West')

for song in artist.songs:
    lyrics = song.lyrics
    with open(f'data/lyrics/{song.title}.txt', 'w') as f:
        f.write(lyrics)
