from word_tools import *

# source = load_string_from_txt("lc_journals.txt")

source = '"This is a sentence." "So is this." And so is this.'

ss = split_into_sentences(source)

print(ss)

# a_sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."

# some_words = split_into_words(a_sentence)
# reversed_words = reverse_list(some_words)
# print(reversed_words)
