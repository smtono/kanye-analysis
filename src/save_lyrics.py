"""
This script is used to extract the lyrics object from the JSON objects located in src/data/lyrics
These lyrics are then written to text files, and stored in the database after light cleaning of Genius artifacts
"""

# Save lyrics
#  Read in lyrics from JSON
import json
import sqlite3
import os

lyrics = {} # Store lyrics from json files

directory = os.fsencode(os.path.join(os.getcwd(), 'src', 'data', 'lyrics'))

for file in os.listdir(directory): # Iterate through lyrics json files
     filename = os.fsdecode(file)
     if filename.endswith(".json"):
         data = json.load(open(os.path.join(os.getcwd(), 'src', 'data', 'lyrics', filename), 'r'))
         
         # Clean song title
         song_title = filename.replace('_lyrics.json', '')
         
         # Store Data
         lyrics[song_title]['lyrics'] = data['lyrics'] # lyrics
         lyrics[song_title]['year'] = data['release_date_components']['year'] # year
         
         continue
     else:
         continue

# Saving lyrics

# Database config
connector = sqlite3.connect(os.path.join(os.getcwd(), 'src', 'data', 'lyrics.db'))
database = connector.cursor()

for key, value in lyrics.items():
    song = key
    lyrics = value['lyrics']

    # TODO: clean lyrics

    # Save song, info, and lyrics to DB
    database.execute(f"INSERT INTO kanye VALUES ('{song}', {0}, '{lyrics}')")
