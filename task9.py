# The simplest way to vectorize text is to use word frequencies.
# Write a function that counts the frequency of each word in a given text.


import re
import string

def word_frequencies(text):
    """
    Count the frequency of each word in the given text.

    >>> word_frequencies("Hello world! Hello AI.")
    {'hello': 2, 'world': 1, 'ai': 1}
    >>> word_frequencies("Risk and finance, risk and AI.")
    {'risk': 2, 'and': 2, 'finance': 1, 'ai': 1}
    >>> word_frequencies("")
    {}
    """
