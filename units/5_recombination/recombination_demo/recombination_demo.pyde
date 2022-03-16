from word_tools import *

# def rhyme(phrase):    
#     vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    
#     index = -1

#     for i in range(len(phrase) - 1):    
#         if phrase[index] in vowels:
#             index -= 1
#         else:
#             break
                            
#     return index


# my_phrase = "Hello worldo"
# result = rhyme(my_phrase)
# print(result)


# my_other_phrase = "Hello world again"
# result = rhyme(my_other_phrase)
# print(result)



# source = load_string_from_txt("LC.txt")
# words = split_into_words(source)

# for l in range(15):
#     line = []
#     for w in range (10):
#         random_word = choice(words)
#         line.append(random_word)
#     print(recombine_list(line))
    
# save("output.png")    ces + poem_source



block_text = """
This is a block of text. It's not just one sentence.

Here's another
block of text

"""

blocks = split_into_blocks(block_text)

for block in blocks:
    print(">" + block)
