# Save lyrics
#  Read in lyrics from JSON
import json
import sqlite3
import os

# Database config
connector = sqlite3.connect(os.path.join(os.getcwd(), 'src', 'data', 'lyrics.db'))
database = connector.cursor()

info = json.load(open(os.path.join(os.getcwd(), 'src', 'data', 'lyrics', f'lyrics/{song}_lyrics.json)', 'r')))
lyrics = info['lyrics']

# Save lyrics to separate file
with open(f'data/lryics/{song}_lyrics.txt', 'w') as f:
    f.write(lyrics)

# Save song, info, and lyrics to DB
database.execute(f"INSERT INTO kanye VALUES ('{song}', '{album}', {0}, '{lyrics}')")
