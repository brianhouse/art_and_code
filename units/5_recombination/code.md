# Recombination

We've already learned how to use variables to store single strings. To do more complicated manipulation of text, however, we'll need additional structures that can store more than one thing at a time. In Python, these are called *lists* (in other programming languages, they are frequently called arrays). Lists can be generated within a program, but they can also be a means of storing data loaded from external sources. Together with strings, conditional logic, and `for` loops, lists open up new possibilities. Although we will continue to work with text, we will be working in the Processing app, not in the terminal (although the terminal will still work, if you prefer).

Before beginning with these functions, however, you'll need to download and install a Python module and some support files. To do that, check out [Getting Started with word_tools](getting_started.md).


### Functions that return things

Before we get to lists, however, we need to look more closely at functions. So far, most of the functions we've used have produced some kind of output—`circle()` draws a circle on the canvas, for example, and `print()` prints text to the console. Even our custom functions, like `living_room()`, have had an immediate effect on the state of the program by moving the reader into a new state.

However, some functions don't produce an output right away. Instead, they generate some result that you can then use later in your program. One example of this that we've already seen is `random()`—we used it as a substitute for static values in our code, and it did the work of coming up with an unexpected number (eg, `circle(random(400), random(400), random(20, 100))`).

When functions like `random()` are called, they **return** a result. Although we used `random()` directly as an argument to some other function, like `circle()`, we could have done this:

```py
my_random_number = random(100)
```

In this case, we've invented a variable, `my_random_number`, and assigned it to whatever a call to `random()` comes up with, or rather, whatever it **returns**.

Another example of this, of course, is `raw_input()`:
```py
response = raw_input()
```

Here, the function does the work of asking the user for input, and the result is stored in variable that we've named `response`.

The functions from `word_tools` that we'll use to work with text are similar. Whenever we use them, we'll be taking the results and storing them in some new or preexisting variable.



### Strings to lists


Consider the following string, which we'll store in a variable called `a_sentence`:

```py
a_sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."
```

While this is a very interesting sentence to read, there's more that we can do with it than just print it out.

To start with, let's split it into words:

```py
from word_tools import *

a_sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."

some_words = split_into_words(a_sentence)
```

Here, the function `split_into_words()` takes a string as an argument, in this case our variable `a_sentence`. It then chops up and polishes the sentence into individual words—ie shorter strings—and returns them as a list. The variable `some_words` now contains that list.

What is a list?
```py
from word_tools import *

a_sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."

some_words = split_into_words(a_sentence)
print(some_words)
```
```text
['societies', 'have', 'always', 'been', 'shaped', 'more', 'by', 'the', 'nature', 'of', 'the', 'media', 'by', 'which', 'we', 'communicate', 'than', 'by', 'the', 'content', 'of', 'the', 'communication']
```

As you can see in the output, the result is a structure delineated by `[` and `]` that includes a sequence of short strings, ie, words.

A list is a very powerful kind of variable—it's actually more of a meta-variable, because it holds other things. These might be numbers, booleans (aka `True`/`False`), strings, or other objects. This list, called `some_words`, currently has 23 items in it, all of them individual strings.

How do we know there are 23? Well, we can find out like this:
```py
from word_tools import *

a_sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."

some_words = split_into_words(a_sentence)
num_words = len(some_words)
print(num_words)
```
```
23
```
`len()` is a function that returns the length of a list. In this case, that's the number of words in the sentence, so we put it in a new variable that we've named `num_words` and printed to the console.

### Reordering and recombining

What else can we do with a list of words?

How about sort them alphabetically:
```py
from word_tools import *

a_sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."

some_words = split_into_words(a_sentence)
sorted_words = sort_list_alpha(some_words)
print(sorted_words)
```
```text
['always', 'been', 'by', 'by', 'by', 'communicate', 'communication', 'content', 'have', 'media', 'more', 'nature', 'of', 'of', 'shaped', 'societies', 'than', 'the', 'the', 'the', 'the', 'we', 'which']
```

...or by length:
```py
from word_tools import *

a_sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."

some_words = split_into_words(a_sentence)
sorted_words = sort_list_length(some_words)
print(sorted_words)
```
```text
['by', 'of', 'by', 'we', 'by', 'of', 'the', 'the', 'the', 'the', 'have', 'been', 'more', 'than', 'media', 'which', 'always', 'shaped', 'nature', 'content', 'societies', 'communicate', 'communication']
```

...or reverse them:
```py
from word_tools import *

a_sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."

some_words = split_into_words(a_sentence)
reversed_words = reverse_list(some_words)
print(reversed_words)
```
```text
['communication', 'the', 'of', 'content', 'the', 'by', 'than', 'communicate', 'we', 'which', 'by', 'media', 'the', 'of', 'nature', 'the', 'by', 'more', 'shaped', 'been', 'always', 'have', 'societies']
```

Or, even better, randomize the order:
```py
from word_tools import *

a_sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."

some_words = split_into_words(a_sentence)
unique_words = filter_unique(some_words)
randomized_words = randomize_list(unique_words)
print(randomized_words)
```
```text
['content', 'by', 'shaped', 'communication', 'been', 'more', 'the', 'of', 'have', 'always', 'than', 'societies', 'which', 'communicate', 'nature', 'media', 'we']
```

And now might be a good time to stick these words back together into a string. We can do that with `recombine_list()`:
```py
from word_tools import *

a_sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."

some_words = split_into_words(a_sentence)
unique_words = filter_unique(some_words)
randomized_words = randomize_list(unique_words)

new_string = recombine_list(randomized_words)
print(new_string)
```
```text
by nature content communication more of the we which media shaped have communicate been than always societies
```
The result is a new string—it's no longer a list—with all the pieces put back together.


### Filter functions

There were a lot of duplicates when we sorted our words. What if we wanted to know the number of **unique** words in the sentence?

In this case, we're going to use a filter function to create a **new** list that contains only unique words:
```py
from word_tools import *

a_sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."

some_words = split_into_words(a_sentence)
num_words = len(some_words)
print(num_words)

unique_words = filter_unique(some_words)
num_unique_words = len(unique_words)
print(num_unique_words)
```
```
23
17
```
Now we know that there are 17 different words in our 23-word-long sentence.

Notice the use of variables in this program. There are a lot of them, and we're creating them to hold particular lists or numbers as we go. And we're naming them descriptively—remember, there's nothing special about the name of a variable (we could be naming them "bananas" and "jupiter") other than it helps us keep track of what it is that we're putting into them.

What if we wanted to filter out all the words that start with the letter "c"?

```py
from word_tools import *

a_sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."

some_words = split_into_words(a_sentence)
c_words = filter_starts_with(some_words, "c")  # first argument is the list, second argument is the letter
print(c_words)
```
```
['communicate', 'content', 'communication']
```
Here, the function `filter_starts_with()` takes two parameters: the list, and the letter (or letters) to test for.

Even more usefully, we could filter for parts of speech:

```py
from word_tools import *

a_sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."

some_words = split_into_words(a_sentence)

nouns = filter_nouns(some_words)
print(nouns)

verbs = filter_verbs(some_words)
print(verbs)
```
```
['societies', 'more', 'nature', 'media', 'content', 'communication']
['have', 'shaped', 'communicate', 'content']
```
Now we have two lists: one with the nouns in the sentence, and one with the verbs. Notice, however, that "content" appears in both lists! The reality is that a language like English resists easy programmatic categorization—there will always be weird exceptions. The algorithm we're using isn't smart enough to analyze the context of a word, it's just checking a dictionary—and "content" can be used as both a noun and a verb (CON-tent vs con-TENT). Thus it's in both lists.

Here are all the filters available to us out of the box:
```py
filter_unique(words)
filter_starts_with(words, s)
filter_ends_with(words, s)
filter_contains(words, s)
filter_nouns(words)
filter_singular_nouns(words)
filter_plural_nouns(words)
filter_verbs(words)
filter_imperative_verbs(words)
filter_past_tense_verbs(words)
filter_present_tense_verbs(words)
filter_adjectives(words)
filter_pronouns(words)
filter_prepositions(words)
filter_interjections(words)
filter_distinctive(words)  # more on this one later
```

The important thing to realize is how these can all be chained together. You might find all the unique verbs that start with the letter "a," for example. Starting with a list of all words, you create new variables for new lists that increasingly refine what you're looking for.


### Iterating through lists

So far, when we have a list of words, we've just been printing them out as a list:

```py
from word_tools import *

a_sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."
some_words = split_into_words(a_sentence)
print(some_words)
```
```text
['societies', 'have', 'always', 'been', 'shaped', 'more', 'by', 'the', 'nature', 'of', 'the', 'media', 'by', 'which', 'we', 'communicate', 'than', 'by', 'the', 'content', 'of', 'the', 'communication']
```

However, we can also print out each word individually using a loop:
```py
from word_tools import *

a_sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."
some_words = split_into_words(a_sentence)

for word in some_words:
    print(word)
```
```
societies
have
always
been
shaped
more
by
the
nature
of
the
media
by
which
we
communicate
than
by
the
content
of
the
communication
```

This is a new syntax for loops that we haven't seen before. Previously, it was like this:
```py
for i in range(10):
    # do something
```
This is essentially saying, "for every integer in the range 0 to 10, do something".

Now we have this:
```py
for word in some_words:
    # do something
```
...which means, "for every word in the some_words list, do something".

The key thing to realize here is that `word` is a variable that changes with every iteration of the loop, just like `i`. But where `i` was a number, `word` is the content of the list itself, in this case the word.


### Working with external text

So far, we've just been playing with a sentence that we've written into the code. But the real interesting stuff here is when we can use text from another source. Anything might work: a newspaper article, messages from social media, or even a whole book.

The key thing is that the text has to be in "Plain Text" format—no Word files here. But most word processor programs, Word and Google Docs included, have the capacity to save files as plain text. So you could copy the contents of an entire webpage, for example, paste it into Google Docs, and download it as a `.txt` file.

In addition, there are online repositories that already have archives of text files, perhaps most notably the [Gutenberg Project](https://www.gutenberg.org). We can download a book in plain text format, such as [_History of the Expedition under the Command of Captains Lewis and Clark, Vol. I._](https://www.gutenberg.org/ebooks/16565) If you click on "Plain Text UTF-8", the text will open in the browser. If you're using Google Chrome, you can just save the file. In Safari, make sure you give it a title that ends in ".txt" (like "LC.txt") and choose "Page Source" instead of "Web Archive".

To copy any text file into your sketch and make it accessible to your code, use Processing's "Add File..." menu option:

<p align="center">
  <img src="code/1_add_file.png" width=200 />
</p>

Then you can load it in using the `load_string_from_txt()` function,:

```py
from word_tools import *

source = load_string_from_txt("LC.txt")
```

The variable `source` now contains the complete text—an enormous string!


### Cut-ups with sentences

Now that we've cleaned the text, we're ready to work with it. Instead of dividing it into words, let's split it into sentences:

```py
from word_tools import *

source = load_string_from_txt("LC.txt")
sentences = split_into_sentences(source)
```

How many sentences do we have? `len()` will tell us:

```py
from word_tools import *

source = load_string_from_txt("LC.txt")
sentences = split_into_sentences(source)

num_sentences = len(sentences)
print(num_sentences)
```
```
5348
```

That's a lot of sentences. Let's grab a random one with the `choice()` function:

```py
from word_tools import *

source = load_string_from_txt("LC.txt")
sentences = split_into_sentences(source)

random_sentence = choice(sentences)
print(random_sentence)

```
```text
More bald eagles are seen on this part of the Missouri than we have previously met with; the small or common hawk, common in most parts of the United States, are also found here: great quantities of geese are feeding in the prairies, and one flock of white brant or goose with black wings, and some gray brant with them pass up river, and from their flight they seem to proceed much farther to the northwest.
```

(This text has some beefy sentences.)

`choice()` is incredibly useful for recombination, because it selects one item from a list of possibilities.

We can use `choice()` to reproduce the cut-up technique by taking several random sentences and piecing them together to form a new text.

To do that, however, we're going to need to create an empty list, called `cut_up`. We do it like this:
```py
cut_up = []
```
We'll also need to know how to add things to this new list. To do it, we use a special function called a method that is connected to the function name with a ".". We've seen methods before in a few situations, and we'll talk about it more later. But for now, just know that we add an item to a list like this:
```py
cut_up.append(sentence)
```

The final ingredient is something we already know how to do: make a loop. If we want to add fives sentences to our cut-up recombination, we'll have to select a sentence and add it to the list, and then repeat that procedure five times. Here's the resulting code:

```py
from word_tools import *

source = load_string_from_txt("LC.txt")
sentences = split_into_sentences(source)

cut_up = [] # make a new list
for i in range(5):
    random_sentence = choice(sentences) # choose a sentence
    cut_up.append(random_sentence) # add the sentence to the list

# recombination the list into a string
result = recombine_list(cut_up)

print(result)
```
```text
The Tetons of the burnt woods. We passed some ancient lodges of driftwood which do not appear to have been lately inhabited. The old guide who had been sent on by captain Clarke, now confirmed, by means of our interpreter, what he had already asserted, of a road up Berry creek which would lead to Indian establishments on another branch of the Columbia: his reports however were contradicted by all the Shoshonees. Sunday 19. The usual appearances of coal, or carbonated wood, and pumicestone still continue, the coal being of a better quality and when burnt affords a hot and lasting fire, emitting very little smoke or flame.
```

While the result is not exactly linearly coherent, we do indeed get a sense of the tenor of the text.


### Filtering sentences

Let's use a filter to find all of the sentences that have to do with wolves. In this case, we're filtering sentences instead of words. Because we want to include sentences that contain "wolf" as well as "wolves", we can run two filters and concatenate the results together using "+":

```py
from word_tools import *

source = load_string_from_txt("LC.txt")
sentences = split_into_sentences(source)

wolf_sentences = filter_contains(sentences, "wolf") + filter_contains(sentences, "wolves")

for sentence in wolf_sentences:
    print(sentence)
    print("")
```
```text
Some men were sent for the meat killed yesterday which fortunately had not been discovered by the wolves.

As soon as we had kindled our fires we examined the meat which captain Clarke had left here, but found that the greater part of it had been taken by the wolves.

A large herd of buffaloe came near us and we procured three of them: besides which were killed two wolves and three antelopes.

Sometimes too they are made of beaver, moonax, and small wolves, and frequently during the summer of elk skin.
```    

### Using text as a vocabulary: free verse poetry

The cut-ups and filters work with external text on the level of sentences, but of course everything we learned about manipulating words still applies. One way to think of it is that a source text can also be used to provide a _vocabulary_ for new texts.

For example, let's take all the _words_ from the LC expedition and randomly recombine them into some free verse poetry.

This is going to require some loops. Say we want 5 lines of 5 words each. We'll have an outer loop for the lines and an inner loop for the words. The inner loop will collect five words into a list and then recombine them before printing them out.

```py
from word_tools import *

source = load_string_from_txt("LC.txt")
words = split_into_words(source)

for l in range(5):
    line = []
    for w in range(5):
        random_word = choice(words)
        line.append(random_word)
    print(recombine_list(line))
```

```
reaching their without with in
by i the engaged settlements
two act the with their
of to the called time
their eastern and encamp situation
```

These words never appeared in the text in this order. Nonethless, together they give a certain feel for the text, even if it's a little nonsensical.

However, there are a lot of words here that are not that distinctive: with, in, by, of, to

In computer science, these are called "stop words." For an application like this, we might want to filter these out _before_ running our free verse algorithm. We have a filter function for that: `filter_distinctive()`

```py
from word_tools import *

source = load_string_from_txt("LC.txt")
words = split_into_words(source)
words = filter_distinctive(words)

for l in range(5):
    line = []
    for w in range(5):
        random_word = choice(words)
        line.append(random_word)
    line = recombine_list(line)
    print(line)
```    
```
route large weapons accompanied conduct
close buffaloe fast various natural
execution tour number day body
one destruction uncommon take produced
clark river two wide authority
```

This is a much more powerful result.


### Using text as a vocabulary: mad libs

Of course, these free verse lines do not adhere to grammatical syntax. We could do that, however, if we selected nouns, verbs, adjectives, and so forth from the text and recombined them according to a template (aka Mad Libs):

```py
from word_tools import *

source = load_string_from_txt("LC.txt")
words = split_into_words(source, max=1000)  # restrict number of words to speed things up
words = filter_distinctive(words)

nouns = filter_singular_nouns(words)
verbs = filter_past_tense_verbs(words)
adjectives = filter_adjectives(words)

for i in range(10):
    madlib = "I " + choice(verbs) + " the " + choice(nouns) + " and " + choice(verbs) + " the " + choice(nouns) + "."
    print(madlib)

```
```text
I sketched the original and kept the order.
I included the ocean and united the public.
I prepared the river and accumulated the way.
I produced the ocean and confined the little.
I prepared the editor and preceded the learning.
I united the government and deposited the press.
I changed the possible and might the order.
I perused the residence and compelled the work.
I upset the whole and began the setting.
I painted the winter and encamped the cache
```

Note that filtering a large number of words by various parts of speech is going to go slow—including an argument "max=1000" in `split_into_words()` limits the vocabulary, but it makes things go faster.


### Using text as a vocabulary: haiku

This example uses the vocabulary from a source text to create a poem in haiku form: 3 lines of 5, 7, and 5 syllables, respectively.

There are some more advanced uses of syntax in this example, as it combines a nested `for` loop with multiple `if` statements, and keeps track of the syllable count with variables.

```py
from word_tools import *

source = load_string_from_txt("LC.txt")
words = split_into_words(source)  # restrict number of words to speed things up
words = filter_distinctive(words)

# remaining_syllables will be 5, 7, and 5 on each iteration of the loop
for remaining_syllables in [5, 7, 5]:
    # shuffle the words
    words = randomize_list(words)

    line = []
    # check every word if necessary
    for word in words:
        # if the syllables in this word are less than the remaining needed, add it
        num_syllables = count_syllables(word)
        if num_syllables <= remaining_syllables:
            line.append(word)
            remaining_syllables -= num_syllables

        # if all syllables are accounted for, "break" the loop
        if remaining_syllables <= 0:
            break
    # combine and print this line        
    print(recombine_list(line))        
```    
```
advantageously
within troubled commanded
oars river ten birds
```
```
approach opposite
arrival apprehensions
minister us night
```
```
idolatry lost
soon soil preparing water
thence bear first  lived
```
