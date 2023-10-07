#!/usr/bin/python3


# returns a tuple with the length of a string
# and its first character.
def multiple_returns(sentence):
    first_character = ''
    sentence_lenght = len(sentence)
    if sentence_lenght != 0:
        first_character = sentence[0]
    else:
        first_character = None
    return (sentence_lenght, first_character)
