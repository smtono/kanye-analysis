"""
Analysis of the music, since the Twitter API is borked, and Kanye is banned, that is kind of going out the window.

!!!!! FEBRUARY 9, THE TWITTER API WILL BE A PAID SERVICE SO THAT IS NOT AN OPTION ANYMORE !!!!!

Instead, I will analyze the lyrics of Kanye's songs, and see if I can find any patterns in his lyrics.
We will do this by analyzing a few things:
-Toxicity using Google Perspective
-Sentiment (using something)
-Word frequency
-IDK WHAT ELSE WHATEVER DUDE
"""

import nltk

"""
Each of these functions will read the lyrics line by line
    LINES ARE BROKEN DOWN BEFORE SENT TO THESE FUNCTIONS
Each line will be analyzed, and the song overall will be an average of the lines
"""

def find_toxicity(lines: list) -> float:
    """
    Uses Google Perspective to find the toxicity of a string of text
    
    Iterate through lines of text, performing toxicity analysis on each line
    Find average at the end to get the toxicity for the whole song
    """

def find_sentiment(lines: list) -> float:
    """
    Uses Google Natural Language to find the sentiment of a string of text
    
    Iterate through lines of text, performing sentiment analysis on each line
    Find average at the end to get the sentiment for the whole song
    """

def find_word_frequency(lines: list) -> float:
    """
    Uses NLTK to find the frequency of words in a string of text
    
    Iterate through lines of text, performing word frequency analysis on each line
    Find average at the end to get the word frequency for the whole song
    """
    # https://www.nltk.org/book/ch01.html
    
