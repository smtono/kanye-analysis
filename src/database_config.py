import sqlite3
import os

# Database config
connector = sqlite3.connect(os.path.join(os.getcwd(), 'src', 'data', 'lyrics.db'))
database = connector.cursor()

database.execute(
    "CREATE TABLE IF NOT EXISTS "
    "kanye "
    "(song TEXT, album TEXT, year INT, lyrics TEXT)"
)
