# import re
from random import choice, shuffle

_stop_words = open("list_stop_words.txt").read().split()
_nouns = open("list_nouns.txt").read().split()
_verbs = open("list_verbs.txt").read().split()
_adjectives = open("list_adjectives.txt").read().split()
_pronouns = open("list_pronouns.txt").read().split()
_prepositions = open("list_prepositions.txt").read().split()
_interjections = open("list_interjections.txt").read().split()

def load_text(filename):
    return " ".join(open(filename).read().split())

def get_sentences(text):
    # text = re.split('. |! |? |." |!" |?"', text)
    text = text.split(". ")
    return text

def get_words(text):
    punctuation_marks = [".", ",", "?", "!", ";", ":", "(", ")", '"', "<", ">", "/", "[", "]", "|", "\\"]
    for i in range(len(punctuation_marks)):
        text = text.replace(punctuation_marks[i], "")
    words = text.lower().split()
    shuffle(words)
    words = words[:2000]
    return words

def get_good_words(words):
    if type(words) != list:
        return None
    return [word for word in words if word not in _stop_words]

def get_nouns(words):
    if type(words) != list:
        return None
    return [word for word in words if word in _nouns]

def get_verbs(words):
    if type(words) != list:
        return None
    return [word for word in words if word in _verbs]

def get_adjectives(words):
    if type(words) != list:
        return None
    return [word for word in words if word in _adjectives]

def get_pronouns(words):
    if type(words) != list:
        return None
    return [word for word in words if word in _pronouns]

def get_prepositions(words):
    if type(words) != list:
        return None
    return [word for word in words if word in _prepositions]

def get_interjections(words):
    if type(words) != list:
        return None
    return [word for word in words if word in _interjections]

def get_unique(words):
    if type(words) != list:
        return None
    return list(set(words))

def combine(words, delimiter=None):
    if delimiter is None:
        delimiter = " "
    return delimiter.join(words)
