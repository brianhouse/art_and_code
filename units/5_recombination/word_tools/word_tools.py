# -*- coding: utf-8 -*-
from random import choice, shuffle

_stop_words = open("list_stop_words.txt").read().split()
_nouns = open("list_nouns.txt").read().split()
_verbs = open("list_verbs.txt").read().split()
_adjectives = open("list_adjectives.txt").read().split()
_pronouns = open("list_pronouns.txt").read().split()
_prepositions = open("list_prepositions.txt").read().split()
_interjections = open("list_interjections.txt").read().split()

def load_text(filename):
    return fix_quotes(" ".join(open(filename).read().split()))

def load_lines(filename):
    return [fix_quotes(line.strip()) for line in open(filename).readlines()]

def load_srt(filename):
    lines = load_lines(filename)
    return combine([line for line in lines if len(line) and line[0] not in "0123456789"])

def get_sentences(text):
    assert(type(text) is str)
    text = text.replace("Mr.", "Mr")
    text = text.replace("Mrs.", "Mrs")
    text = text.replace("Ms.", "Ms")
    for delim in (". ", "! ", "? ", '." ', '?" ', '!" '):
        text = text.replace(delim, delim + "^^^")
    return text.split(" ^^^")

def fix_quotes(text):
    assert(type(text) is str)
    text = text.replace('“', '"')
    text = text.replace('”', '"')
    text = text.replace("’", "'")
    text = text.replace("‘", "'")
    text = text.replace("–", "-")
    text = text.replace("—", " -- ")
    text = text.replace("…", "...")
    text = text.replace("  ", " ")
    text = text.replace("  ", " ")
    return text

def remove_punctuation(text):
    assert(type(text) is str)
    for mark in (".", ",", "?", "!", ";", ":", "(", ")", '"', "<", ">", "/", "[", "]", "|", "\\", "{", "}", "+", "*"):
        text = text.replace(mark, "")
    return text

def get_words(text, max_words=5000):
    assert(type(text) is str)
    text = remove_punctuation(text)
    words = text.lower().split()
    words = words[:max_words]
    return words

def get_good_words(text, max_words=5000):
    words = get_words(text)
    return [word for word in words if word not in _stop_words]

def get_nouns(words):
    assert(type(words) is list)
    return [word for word in words if word in _nouns]

def get_verbs(words):
    assert(type(words) is list)
    return [word for word in words if word in _verbs]

def get_adjectives(words):
    assert(type(words) is list)
    return [word for word in words if word in _adjectives]

def get_pronouns(words):
    assert(type(words) is list)
    return [word for word in words if word in _pronouns]

def get_prepositions(words):
    assert(type(words) is list)
    return [word for word in words if word in _prepositions]

def get_interjections(words):
    assert(type(words) is list)
    return [word for word in words if word in _interjections]

def get_unique(words):
    assert(type(words) is list)
    return list(set(words))

def combine(words, delimiter=None):
    assert(type(words) is list)
    if delimiter is None:
        delimiter = " "
    return delimiter.join(words)

def replace(text, find, rep):
    assert(type(text) is str)
    return text.replace(find, rep)

def remove(text, find):
    assert(type(text) is str)
    return text.replace(find, "")


"""
"string_from_txt"
"lines_from_txt"
"lines_from_srt"

split_words
split_sentences

filter_distinctives
filter_nouns
filter_unique

combine_list ?

change assertion error to:
"Expecting list, got string"
"Expecting string, got list"

separate verb types
filter_verbs(type="past") ?
chop possessives

should strip punctuation from ends of words, not remove it entirely

/

adding lists of words together

have the results of the examples on the page

sort is actually not that interesting. by len is more interesting.

lessons (focus on list operations):
- using brackets
- using brackets on string (check first letter is capital maybe)
- making your own filter
- finding clues in sentences <-- how to do this





"""
