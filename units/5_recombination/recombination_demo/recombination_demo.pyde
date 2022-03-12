from word_tools import *

beef_source = load_string_from_txt("beef.txt")
poem_source = load_lines_from_txt("Phenomenal_Woman.txt")

beef_sentences = split_into_sentences(beef_source)
combined_sentences = beef_sentences + poem_source
