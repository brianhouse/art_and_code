from word_tools import *

source = load_string_from_txt("LC.txt")
words = split_into_words(source)  # restrict number of words to speed things up
words = filter_distinctive(words)

for remaining_syllables in [5, 7, 5]:
    words = randomize_list(words) 
    line = []
    for word in words:
        num_syllables = count_syllables(word)
        if num_syllables <= remaining_syllables:
            line.append(word)
            remaining_syllables -= num_syllables
        if remaining_syllables <= 0:
            break
    print(recombine_list(line))        
    
