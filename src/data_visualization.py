"""
This module is used to define functions used to aid in data visualization
These include:
    - Lexical dispersion plot
    - Word cloud
    - Sentiment analysis
"""

from nltk.book import *

def lexical_dispersion(text: str, words: list):
    """
    Creates a visualization of where words appear in text
    """

def frequency_distribution(text: str):
    """
    Creates a visualization of the frequency of words in text
    """
    FreqDist(text).plot(50, cumulative=False)
