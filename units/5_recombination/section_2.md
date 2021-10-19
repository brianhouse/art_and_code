## Helper functions and examples

Add the following files to your sketch:

#### Helper functions
- [helpers.py](helpers.py)


#### Word lists
- [list_stop_words.txt](list_stop_words.txt)  
- [list_adjectives.txt](list_adjectives.txt)
- [list_interjections.txt](list_interjections.txt)
- [list_nouns.txt](list_nouns.txt)
- [list_prepositions.txt](list_prepositions.txt)
- [list_pronouns.txt](list_pronouns.txt)
- [list_verbs.txt](list_verbs.txt)


### Examples

```py
from random import choice
from helpers import load_text, get_sentences, get_words, get_good_words, get_unique, get_verbs, get_adjectives, get_nouns

lclark = load_text("LC.txt")
starbucks = load_text("starbucks.txt")
```

```py
# verbs from one, nouns from another
lclark_words = get_words(lclark)
starbucks_words = get_words(starbucks)
verbs = get_verbs(starbucks_words)
nouns = get_nouns(lclark_words)
print("The digital media class " + choice(verbs) + " the " + choice(nouns) + ".")
```

```py
# interleaved sentences
lclark_sentences = get_sentences(lclark)
starbucks_sentences = get_sentences(starbucks)
paragraph = []
for i in range(2):
    sentence = choice(lclark_sentences)
    paragraph.append(sentence)
    sentence = choice(starbucks_sentences)
    paragraph.append(sentence)
result = ". ".join(paragraph)
print(result)
```
