"""
This script is used to scrape lyrics from all of Kanye's songs using the Genius API.
"""

import os
from lyricsgenius import Genius

genius = Genius(access_token=os.environ['GENIUS_ACCESS_TOKEN'])

