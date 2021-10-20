## Helper functions and examples

Add the following files to your sketch:

#### Helper functions
- [word_tools.py](word_tools/word_tools.py)


#### Word lists
- [list_stop_words.txt](list_stop_words.txt)
- [list_adjectives.txt](list_adjectives.txt)
- [list_interjections.txt](list_interjections.txt)
- [list_nouns.txt](list_nouns.txt)
- [list_prepositions.txt](list_prepositions.txt)
- [list_pronouns.txt](list_pronouns.txt)
- [list_verbs.txt](list_verbs.txt)


### Examples

Madlibs:
```py
from word_tools import *

text = load_text("LC.txt")  # load whole book as a string
words = get_words(text)     # divide the string into words
nouns = get_nouns(words)    # separate out the nouns
verbs = get_verbs(words)    # separate out the verbs
print("The digital media class " + choice(verbs) + " the " + choice(nouns) + ".")   # recombine
```

Interleaving two texts:
```py
from word_tools import *

# load two different texts
lclark = load_text("LC.txt")
starbucks = load_text("starbucks.txt")

# split both strings into lists of sentences
lclark_sentences = get_sentences(lclark)        
starbucks_sentences = get_sentences(starbucks)

# alternate picking random sentences from both lists
paragraph = []
for i in range(5):
    sentence = choice(lclark_sentences)
    paragraph.append(sentence)
    sentence = choice(starbucks_sentences)
    paragraph.append(sentence)
result = ". ".join(paragraph)
print(result)
```

Loading a file into separate lines (good for poetry, lyrics, legal documents, and other sources that aren't made up of sentences):
```py
from word_tools import *

# load a text into a list of lines
lines = load_lines("stairway.txt")

print(choice(lines))
```

Filtering for sentences that include the word "buffaloe":
```py
from word_tools import *

LC_text = load_text("LC.txt")

sentences = get_sentences(LC_text)
buffaloe_sentences = []
for i in range(len(sentences)):
    sentence = sentences[i]
    if "buffaloe" in sentence:
        buffaloe_sentences.append(sentence)

if len(buffaloe_sentences):                
    print(choice(buffaloe_sentences))        
else:
    print("No sentences found!")
```

Filtering for words that include a price:
```py
from word_tools import *

nyt_text = load_text("tech.txt")   

words = get_words(nyt_text)
money_words = []
for i in range(len(words)):
    word = words[i]
    if "$" in word:
        money_words.append(word)

if len(money_words):        
    print(choice(money_words))
else:
    print("No prices found")  
```
