"""
This script is used to extract the lyrics object from the JSON objects located in src/data/lyrics
These lyrics are then written to text files, and stored in the database after light cleaning of Genius artifacts

The goal of this script is to extract the LYRICS data points from the JSON files, and store them in a database
Alongside the song title, and year of release
This will be achieved by iterating through the JSON files, and extracting the lyrics object

- Iterate through the JSON files
- Extract the lyrics object
- Clean the lyrics object
- Initialize the DB
- Save the lyrics to teh DB
"""

# Save lyrics
#  Read in lyrics from JSON
import json
import sqlite3
import os

# Iterate Files
lyrics_dict = {} # Store lyrics from json files

directory = os.fsencode(os.path.join(os.getcwd(), 'src', 'data', 'lyrics'))

for file in os.listdir(directory): # Iterate through lyrics json files
     filename = os.fsdecode(file)
     if filename.endswith(".json"):
         data = json.load(open(os.path.join(os.getcwd(), 'src', 'data', 'lyrics', filename), 'r'))

         # Store Data
         lyrics_dict[f"{data['title']}"] = {}
         lyrics_dict[f"{data['title']}"]['lyrics'] = data['lyrics']
         lyrics_dict[f"{data['title']}"]['year'] = data['release_date_components']['year']

     else:
         continue

# Clean Lyrics
delimeter = ['.', '!', '?', 
             '\n', '\r', '\t',
             '[', ']', '(', ')']

for key, value in lyrics_dict.items():
    song = key
    lyrics = value['lyrics']

    # Clean Lyrics
    # TODO: fix this
    for char in delimeter:
        lyrics = lyrics.replace(char, '')

    # Save cleaned lyrics
    lyrics_dict[f"{song}"]['lyrics'] = lyrics

# Database config
connector = sqlite3.connect(os.path.join(os.getcwd(), 'src', 'data', 'lyrics.db'))
database = connector.cursor()

for key, value in lyrics_dict.items():
    song = key
    lyrics = value['lyrics']

    # Save song, info, and lyrics to DB
    query = f"INSERT INTO kanye VALUES ('{song}', '{lyrics}')"
    database.execute(query)
