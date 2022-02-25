from word_tools import *

source = load_string_from_txt("lc_journals.txt")

sentences = split_into_sentences(source)
for sentence in sentences:
    print(sentence)
    print("")
