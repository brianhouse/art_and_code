# Recombination

We've already learned how to use variables to store single strings. To do more complicated manipulation of text, however, we'll need additional structures that can store more than one thing at a time. In Python, these are called *lists* (in other programming languages, they are frequently called arrays). Lists can be generated within a program, but they can also be a means of storing data loaded from external sources. Together with strings, conditional logic, and `for` loops, lists open up new possibilities. Although we will continue to work with text, we will be working in the Processing app, not in the terminal (although the terminal will still work, if you prefer).

If you haven't already, [get started with word_tools](getting_started.md) before continuing here.

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
```
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
```
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
```
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
```
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
```
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
```
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
filter_nouns(words)
filter_verbs(words)
filter_adjectives(words)
filter_pronouns(words)
filter_prepositions(words)
filter_interjections(words)
filter_distinctive(words)  # more on this one later
```

The important thing to realize is how these can all be chained together. You might find all the unique verbs that start with the letter "a," for example. Starting with a list of all words, you create new variables for new lists that increasingly refine what you're looking for.

### Custom filters (and counting syllables)

However, we can also write our filters.

Consider the following fabulous function, which determines the number of syllables in a word (again—it's not a very smart function, so this might be approximate).

It works like this:
```py
from word_tools import *

a_word = "nature"
num_syllables = count_syllables(a_word)
print(num_syllables)
```
```
2
```

```md
/
choice + madlibs (w/ recombining)
count_syllables



then move on to external text

cut-ups with sentences
joining

filters on sentence level:
starts with
ends with
nouns etc
get_string_before
get_string_after
replace_in_string (capitalism)

words again:
good_words

haiku example

////

advanced examples:

structure:
- free verse poem
- by line length

combine two texts
- by line
- by part of speech
- filter one text by another


////

books
wikipedia articles
transcribed audio
legal texts / laws / contracts
movies: scripts, closed-captioning
lyrics
newspaper articles
social media feeds
```
