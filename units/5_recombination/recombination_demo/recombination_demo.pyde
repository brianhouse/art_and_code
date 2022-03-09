from word_tools import *

endurance_source = load_string_from_txt("endurance.txt")
titanic_source = load_string_from_txt("titanic.txt")

endurance_sentences = split_into_sentences(endurance_source)
titanic_sentences = split_into_sentences(titanic_source)

combined_sentences = endurance_sentences + titanic_sentences

paragraph = []

for i in range(10):
    random_sentence = choice(combined_sentences)
    paragraph.append(random_sentence)
    

result = recombine_list(paragraph)
print(result)    
