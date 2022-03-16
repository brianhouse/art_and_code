# -*- coding: utf-8 -*-
import re
from random import choice, shuffle

stop_words_list = open("stop_words.txt").read().split()
plural_nouns_list = open("nouns_plural.txt").read().split()
nouns_list = open("nouns.txt").read().split()
imperative_verbs_list = open("verbs_imperative.txt").read().split()
past_tense_verbs_list = open("verbs_past.txt").read().split()
present_tense_verbs_list = open("verbs_present.txt").read().split()
adjectives_list = open("adjectives.txt").read().split()
pronouns_list = open("pronouns.txt").read().split()
prepositions_list = open("prepositions.txt").read().split()
interjections_list = open("interjections.txt").read().split()

def load_string_from_txt(filename):
    print("Loading...")
    data = open(filename).read()
    print("--> complete")
    return " ".join(data.split()).replace("“", '"').replace("”", '"').decode("utf-8")

def load_lines_from_txt(filename):
    print("Loading...")
    data = open(filename).readlines()
    print("--> complete")
    return [line.strip().replace("“", '"').replace("”", '"').decode("utf-8") for line in data if len(line.strip())]

def load_blocks_from_txt(filename):
    print("Loading...")
    data = open(filename).read()
    print("--> complete")
    data = data.strip().replace("“", '"').replace("”", '"').decode("utf-8")
    blocks = [block.strip() for block in re.split("\n[\t\n\r ]*\n", data) if len(block.strip())]
    return [" ".join(block.split()) for block in blocks]

def load_lines_from_srt(filename):
    lines = load_lines(filename)
    return recombine_list([line.strip().replace("“", '"').replace("”", '"').decode("utf-8") for line in lines if len(line) and line[0] not in "0123456789"])

def split_into_sentences(text, max=10000):
    if type(text) is not str and type(text) is not unicode:
        raise Exception("Expecting string")
    ps = [0]        
    pattern = "[^ \.A-Z].(\. |\? |! |\.\" |\?\" |!\" )[A-Za-z\"]"
    for split_point in re.finditer(pattern, text):
        p = split_point.start(0) + (3 if '"' not in text[split_point.start(0):split_point.end(0)] else 4)
        ps.append(p)
    sentences = [text[i:j].strip() for i, j in zip(ps, ps[1:] + [None])]
    return sentences[:max] 

def split_into_words(text, max=10000):
    if type(text) is not str and type(text) is not unicode:
        raise Exception("Expecting string")
    words = text.lower().split()
    words = words[:max]
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
    return [word for word in words if word not in stop_words_list]

def filter_nouns(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if (word in nouns_list) or (word in plural_nouns_list)]

def filter_singular_nouns(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word in nouns_list]

def filter_plural_nouns(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word in plural_nouns_list]

def filter_verbs(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if (word in imperative_verbs_list) or (word in past_tense_verbs_list) or (word in present_tense_verbs_list)]

def filter_imperative_verbs(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word in imperative_verbs_list]

def filter_past_tense_verbs(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word in past_tense_verbs_list]

def filter_present_tense_verbs(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word in present_tense_verbs_list]

def filter_adjectives(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word in adjectives_list]

def filter_pronouns(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word in pronouns_list]

def filter_prepositions(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word in prepositions_list]

def filter_interjections(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word in interjections_list]

def filter_starts_with(words, s):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word[:len(s)] == s]

def filter_ends_with(words, s):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if word[-len(s):] == s]

def filter_contains(words, s):
    if type(words) is not list:
        raise Exception("Expecting list")
    return [word for word in words if s in word]

def filter_unique(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    return list(set(words))

def recombine_list(words, delimiter=None):
    if type(words) is not list:
        raise Exception("Expecting list")
    if delimiter is None:
        delimiter = " "
    return delimiter.join(words)

def sort_list_alpha(words, reverse=False):
    if type(words) is not list:
        raise Exception("Expecting list")
    l = words[:]
    l.sort()
    if reverse:
        l.reverse()
    return l

def sort_list_length(words, reverse=False):
    if type(words) is not list:
        raise Exception("Expecting list")
    l = words[:]
    l.sort(key=len)
    if reverse:
        l.reverse()
    return l

def randomize_list(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    l = words[:]
    shuffle(l)
    return l    

def reverse_list(words):
    if type(words) is not list:
        raise Exception("Expecting list")
    l = words[:]
    l.reverse()
    return l    

def get_string_after(text, search):
    index = text.find(search)
    return text[index + len(search):] if index > -1 else text

def get_string_before(text, search):
    index = text.find(search)
    return text[:index] if index > -1 else text

def replace_in_string(text, find, rep):
    if type(text) is not str and type(text) is not unicode:
        raise Exception("Expecting string")
    return text.replace(find, rep)

def remove_from_string(text, find):
    if type(text) is not str and type(text) is not unicode:
        raise Exception("Expecting string")
    return text.replace(find, "")

def count_syllables(word):
    if not len(word):
        return 0
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
    if type(text) is not str or type(text) is unicode:
        raise Exception("Expecting string")
    output = createWriter(filename)
    output.print(text)
    output.flush()
    output.close()
