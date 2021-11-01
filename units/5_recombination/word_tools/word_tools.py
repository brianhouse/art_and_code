# -*- coding: utf-8 -*-
from random import choice, shuffle

_stop_words = open("list_stop_words.txt").read().split()
_nouns = open("list_nouns.txt").read().split()
_verbs = open("list_verbs.txt").read().split()
_adjectives = open("list_adjectives.txt").read().split()
_pronouns = open("list_pronouns.txt").read().split()
_prepositions = open("list_prepositions.txt").read().split()
_interjections = open("list_interjections.txt").read().split()

def load_string_from_txt(filename):
    return fix_quotes(" ".join(open(filename).read().split()))

def load_lines_from_txt(filename):
    return [fix_quotes(line.strip()) for line in open(filename).readlines()]

def load_lines_from_srt(filename):
    lines = load_lines(filename)
    return combine([line for line in lines if len(line) and line[0] not in "0123456789"])

def split_into_sentences(text, max_sentences=1000):
    assert(type(text) is str)
    text = text.replace("Mr.", "Mr@@@@")
    text = text.replace("Mrs.", "Mrs@@@@")
    text = text.replace("Ms.", "Ms@@@@")
    text = text.replace("...", "@@@@@@@@@@@@")
    for delim in (". ", "! ", "? ", '." ', '?" ', '!" '):
        text = text.replace(delim, delim + "^^^^")
    sentences = text.split(" ^^^^")[:max_sentences]
    return [sentence.replace("@@@@", ".") for sentence in sentences]

def split_into_words(text, max_words=5000):
    if type(text) is not str:
        raise Exception("Expecting string")
    words = text.lower().split()
    words = words[:max_words]
    marks = ".", ",", "?", "!", ";", ":", "(", ")", '"', "<", ">", "/", "[", "]", "|", "\\", "{", "}", "+", "*", "-", "&"
    for w, word in enumerate(words):
        while len(word) and word[0] in marks:
            word = word[1:]
        while len(word) and word[-1] in marks:
            word = word[:-1]
        words[w] = word
    words = [word for word in words if len(words)]
    return words

def filter_distinctive(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word not in _stop_words]

def filter_nouns(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word in _nouns]

def filter_verbs(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word in _verbs]

def filter_adjectives(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word in _adjectives]

def filter_pronouns(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word in _pronouns]

def filter_prepositions(words):
    assert(type(words) is list)
    return [word for word in words if word in _prepositions]

def filter_interjections(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word in _interjections]

def filter_starts_with(words, s):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word[:len(s)] == s]

def filter_ends_with(words, s):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word[-len(s):] == s]

def filter_unique(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return list(set(words))

def combine_list(words, delimiter=None):
    if type(words) is not list:
        raise Exception("Expecting list")
    if delimiter is None:
        delimiter = " "
    return delimiter.join(words)

def sort_list_alpha(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    l = words[:]
    l.sort()
    return l

def sort_list_length(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    l = words[:]
    l.sort(key=len)
    return l

def get_string_after(text, search):
    index = text.find(search)
    return text[index + len(search):] if index > -1 else text

def get_string_before(text, search):
    index = text.find(search)
    return text[:index] if index > -1 else text

def replace_in_string(text, find, rep):
    if type(text) is not str:
        raise Exception("Expecting string")
    return text.replace(find, rep)

def remove_from_string(text, find):
    if type(text) is not str:
        raise Exception("Expecting string")
    return text.replace(find, "")

def fix_quotes(text):
    if type(text) is not str:
        raise Exception("Expecting string")
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

def count_syllables(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word[-1] == "e" and (len(word) < 2 or word[-2] != "e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def write_string_to_file(text, filename):
    if type(text) is not str:
        raise Exception("Expecting string")
    output = createWriter(filename)
    output.print(text)
    output.flush()
    output.close()




"""
separate verb types
filter_verbs(type="past") ?
chop possessives on nouns? etc

"""
