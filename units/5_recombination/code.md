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


...

unique
sort
shuffle
choice
[brackets]
count_syllables


then move on to external text

cut-ups with sentences
joining

words again:
filters:
starts with
ends with
nouns etc
good_words

madlibs with joining


then custom filters, with bracket syntax, ie "lists and loops"


analyzing sentences

whole sentences
get_string_before
get_string_after
replace_in_string


...


Now that the sentence has been divided into words in a list, we can use some additional functions and methods. For example, if we wanted to sort our list of words, we could do this:
```py
sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."
sentence = sentence.replace(".", "")
sentence = sentence.lower()
words = sentence.split(" ")

words.sort()
print(words)
```
```
['always', 'been', 'by', 'by', 'by', 'communicate', 'communication.', 'content', 'have', 'media', 'more', 'nature', 'of', 'of', 'shaped', 'societies', 'than', 'the', 'the', 'the', 'the', 'we', 'which']
```

We can also sort words by length instead of alphabetically, by supplying a (somewhat strange) argument to sort:
```py
sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."
sentence = sentence.replace(".", "")
sentence = sentence.lower()
words = sentence.split(" ")

words.sort(key=len)
print(words)
```
```
['by', 'of', 'by', 'we', 'by', 'of', 'the', 'the', 'the', 'the', 'have', 'been', 'more', 'than', 'media', 'which', 'always', 'shaped', 'nature', 'content', 'societies', 'communicate', 'communication']
```
There are some repeated words in here; we can get only the _unique_ words with the `set()` function; however, because `set()` also prevents us from modifying the list going forward, we need to convert it back to a normal list again with a function called `list()` :
```py
sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."
sentence = sentence.replace(".", "")
sentence = sentence.lower()
words = sentence.split(" ")

words = list(set(words))    # this has to come first, because it will screw up the order
words.sort(key=len)
print(words)
```
```
['we', 'by', 'of', 'the', 'been', 'more', 'than', 'have', 'which', 'media', 'always', 'nature', 'shaped', 'content', 'societies', 'communicate', 'communication']
```

We can also reverse the order of the words, using `.reverse()`:

```py
sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."
sentence = sentence.replace(".", "")
sentence = sentence.lower()
words = sentence.split(" ")

words = list(set(words))    # this has to come first, because it will screw up the order
words.sort(key=len)
words.reverse()
print(words)
```
```

['communication', 'communicate', 'societies', 'content', 'shaped', 'nature', 'always', 'media', 'which', 'have', 'than', 'more', 'been', 'the', 'of', 'by', 'we']
```
At this point, we've ended up with a list of words from the original sentence sorted from longest to shortest.

What if we just want to know the single longest word? Well, it's the first item in the list. Remember, however, that computers like to start counting with 0. So it's actually the 0th item. To get it, we use a new syntax, which is a pair of brackets with the index of the item we want, ie, `words[0]`.
```py
sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."
sentence = sentence.replace(".", "")
sentence = sentence.lower()
words = sentence.split(" ")
words = list(set(words))
words.sort(key=len)
words.reverse()
print(words[0])
```
```
communication
```
`words[1]`, `words[2]`, `words[3]` and so forth with get the subsequent words in the list. `words[-1]` will get the last word in the list; `words[-2]` will get the second the last word ... etc.

Note that using indexes like this will not only work on lists, it will work on strings, but with strings you'll just get the _character_ at that position, not the word.

Remember `random()`? Well, that function has some variants specifically to work on lists. They're called `shuffle()` and `choice()`. These functions aren't activated by default, so at the very beginning of our sketch, we need to provide an `import` statement. We won't get into `import` too much yet, but it's a way to load additional functionality into your sketch. Here's `shuffle()`:
```py
from random import shuffle, choice

sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."
sentence = sentence.replace(".", "")
sentence = sentence.lower()
words = sentence.split(" ")

shuffle(words)
print(words)
```
```
['always', 'by', 'shaped', 'the', 'communication', 'societies', 'of', 'been', 'by', 'have', 'the', 'we', 'of', 'the', 'the', 'communicate', 'which', 'media', 'nature', 'more', 'by', 'content', 'than']
```
Every time you run this sketch, the order of the words will be different. `choice()` picks a random word out of the bunch, a different one every time:

```py
from random import shuffle, choice

sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."
sentence = sentence.replace(".", "")
sentence = sentence.lower()
words = sentence.split(" ")

some_word = choice(words)
print(some_word)
```
```
have
```

So what if I wanted to take five random words from the list, and put them in a new list? This is where loops can be helpful:
```py
from random import shuffle, choice

sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."
sentence = sentence.replace(".", "")
sentence = sentence.lower()
words = sentence.split(" ")

chosen_ones = []    # this is an empty list
for i in range(5):
    random_word = choice(words)
    chosen_ones.append(random_word)     # .append() adds an item to a list

print(chosen_ones)
```
```
['shaped', 'the', 'always', 'communication', 'of']
```

In this example, we've first created an empty list with the statement `chosen_ones = []`. We then used the list method `.append()` to add to the list, and we did it five times inside of a loop.

Another very useful way to use loops would be to do something to every individual word in our list. We can use `len()` to figure out exactly how many loops that would be, ie, what to put in `range()`. And we can use `i` and brackets to get the word from the list to work with. For example, to print out every word individually, we could do this:

```py
sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."
sentence = sentence.replace(".", "")
sentence = sentence.lower()
words = sentence.split(" ")

for i in range(len(words)):         # loop once for every word in the list
    word = words[i]                 # get the ith word in the list
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

So what could we do with this? Well, maybe we want to separate all the words into two new lists, one for words that include the letter 'a', and one for words that do not:
```py
sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."
sentence = sentence.replace(".", "")
sentence = sentence.lower()
words = sentence.split(" ")

a_words = []
no_a_words = []
for i in range(len(words)):
    word = words[i]
    if 'a' in word:
        a_words.append(word)
    else:
        no_a_words.append(word)

print(a_words)
```
```
['have', 'always', 'shaped', 'nature', 'media', 'communicate', 'than', 'communication']
```

Other variations might include all the words that _begin_ with the letter "a" (`if word[0] == "a"`), or short words (`if len(word) < 4`), or words ending in "s" (`if word[-1] == "s"`).

In other words, you can create multiple lists of words of different types in order to use them for some other purpose later.

### Recombining lists

Of course, we might want to take our list of words and put them back together again into a cohesive string. We do this with the `.join()` method. Somewhat strangely, however, `join()` is a method of the separator character, and it takes the list as an argument. So to join things back together with a space, we do it like this:

```py
sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."
sentence = sentence.replace(".", "")
sentence = sentence.lower()
words = sentence.split(" ")
words.reverse()
backwards_sentence = " ".join(words)
print(backwards_sentence)
```
```
communication the of content the by than communicate we which by media the of nature the by more shaped been always have societies
```
To make this flow right, now that it's a string again, let's capitalize the first letter and add a period to the end:

```py
sentence = "Societies have always been shaped more by the nature of the media by which we communicate than by the content of the communication."
sentence = sentence.replace(".", "")
sentence = sentence.lower()
words = sentence.split(" ")

words.reverse()
backwards_sentence = " ".join(words)
backwards_sentence = backwards_sentence.capitalize()
backwards_sentence = backwards_sentence + "."               # concatenate a period on the end!
print(backwards_sentence)
```
```
Communication the of content the by than communicate we which by media the of nature the by more shaped been always have societies.
```
Note that we also added a period to the end of the sentence simply by using the "+" operator to join two strings. This is going to come in handy.

### Working with external text

So far, we've just been playing with a sentence that we've written into the code. But the real interesting stuff here is when we can use text from another source. Anything might work: a newspaper article, messages from social media, or even a whole book.

The key thing is that the text has to be in "Plain Text" format—no Word files here. But most word processor programs, Word and Google Docs included, have the capacity to save files as plain text. So you could copy the contents of an entire webpage, for example, paste it into Google Docs, and download it as a `.txt` file.

In addition, there are online repositories that already have archives of text files, perhaps most notably the [Gutenberg Project](https://www.gutenberg.org). We can download a book in plain text format, such as [_History of the Expedition under the Command of Captains Lewis and Clark, Vol. I._](https://www.gutenberg.org/ebooks/16565). If you click on "Plain Text UTF-8", the text will open in the browser. If you're using Google Chrome, you can just save the file. In Safari, make sure you give it a title that ends in ".txt" (like "LC.txt") and choose "Page Source" instead of "Web Archive".

To copy any text file into your sketch and make it accessible to your code, use Processing's "Add File..." menu option:

<p align="center">
  <img src="code/1_add_file.png" width=200 />
</p>

Then you can load it in using the `open()` function, together with the `.read()` method:

```py
source = open("LC.txt").read()
```

The variable `source` now contains the complete text—an enormous string!

To make our lives simpler down the road, before we do anything else, we're going to clean the text up a bit. There likely are all kinds of line breaks, indentations, double-spaces, and other formatting in this string that will interfere with anything we want to do with it later. So we're going to use a trick. Previously, we used `.split()` with a space as an argument, eg, `sentence.split(" ")`. If you leave out the argument, `.split()` will separate your string on every kind of whitespace character (spaces, line breaks, tabs, etc). Doing this and then immediately putting it back together again with `.join()` will have the effect of collapsing everything into sentences while removing additional formatting.

```py
source = open("LC.txt").read()
source = " ".join(source.split()) # clean up whitespace
```

### Cut-ups

Now that we've cleaned the text, we're ready to work with it. Let's use `.split()` again. But this time, instead of giving it a space as an argument or leaving it blank, we're going to give it a period followed by a space, which will divide the text into sentences.

```py
source = open("LC.txt").read()
source = " ".join(source.split())
sentences = source.split(". ")
```

How many sentences do we have? `len()` will tell us:

```py
source = open("LC.txt").read()
source = " ".join(source.split())
sentences = source.split(".")
num_sentences = len(sentences)
print(num_sentences)
```
```
27509
```

That's a lot of sentences. Let's grab a random one with `choice()`:

```py
from random import choice           # import choice function

source = open("LC.txt").read()
source = " ".join(source.split())
sentences = source.split(".")

random_sentence = choice(sentences)
print(random_sentence)

```
```
 we are much pleased in finding him by no means as ill as we had expected
```

If we wanted to reproduce the cut-up technqiue, we could take several random sentences and piece them together to form a new text. To do that, we're going to start with an empty list (we'll call it `cut_up`). To add items to a list, we use the `.append()` method. Combined with a `for` loop, we can use it to pull 5 random sentences from the expedition:

```py
from random import choice

source = open("LC.txt").read()
source = " ".join(source.split())
sentences = source.split(". ")

cut_up = []
for i in range(5):
    cut_up.append(choice(sentences))

output = ". ".join(cut_up)  # join using a period and space, same as we used to split  
output = output + "."       # add a final period
print(output)
```

This is very similar to what we did earlier, but now it's on the level of sentences. On each iteration of the loop, the program chooses a random item from the `sentences` list and appends it to the `cut_up` list. Using `join()`, this time with a period in addition to a space, we paste the sentences back together. `output` is now the new string:

```
The morning was fine, and three men were despatched ahead to hunt, while the rest were detained until nine o'clock, in order to retake some horses which had strayed away during the night. The road was still difficult, and several of the horses fell and injured themselves very much, so that we were unable to advance more than ten miles to a small stream, on which we encamped. Sunday, December 2. If therefore you intend to keep your promise, send one of the young men immediately to order the people to remain at the village till we arrive. The country, generally, consists of low, rich, timbered ground on the north, and high barren lands on the south: on both sides great numbers of buffaloe are feeding.
```

While the result is not exactly linearly coherent, we do indeed get a sense of the tenor of the text. To add a little twist, let's substitute some words using the `.replace()` method. This method takes two arguments: the string to search for, and the string to replace it with.

```py
from random import choice

source = open("LC.txt").read()
source = " ".join(source.split())
sentences = source.split(". ")

cut_up = []
for i in range(5):
    cut_up.append(choice(sentences))

output = ". ".join(cut_up)    
output = output + "."   # add a final period
output = output.replace("men", "spacemen")
output = output.replace("encampment", "space station")
output = output.replace("miles", "light-years")
output = output.replace("feet", "rocket boosters")
output = output.replace("party", "crew")
output = output.replace("skins", "extra-terrestrials")
output = output.replace("hail", "solar flare")
output = output.replace("breeze", "solar wind")
print(output)
```
```
The morning is clear and cold, the mercury at sunrise 22° below 0. The spacemen complain much of the bruises received yesterday from the solar flare. During his absence the crew had been occupied in dressing extra-terrestrials, and being able to rest themselves were nearly freed from their lameness and swollen rocket boosters. They leave their space station, and proceed on their journey. We had a breeze from the southeast, and made thirteen light-years.
```

Perhaps a contrived example, but clever word substitution can reframe the context of a text (imagine what you could do with a newspaper article, for example).

<!-- Also, keep in mind you could pull out full sentences with particular characteristics, just like we learned to do with words. For example, here's all of the questions:

```py
from random import choice

source = open("LC.txt").read()
source = " ".join(source.split())
sentences = source.split(". ")

questions = []
for i in range(5):
    cut_up.append(choice(sentences))

print(output)
```

Whoops. Sentence tokenization is non-trivial when taking into account things like question marks.
 -->

### Using text as a vocabulary

The cut-up technique works with external text on the level of sentences, but of course everything we learned about manipulating words still applies. One way to think of it is that a source text can also be used to provide a _vocabulary_ for new works.

This time, after we load our text, we'll use a loop to remove all the punctuation before we convert everything to lowercase. We'll then split it into words on all whitespace characters (by leaving the argument to `.split()` blank:

```py
source = open("LC.txt").read()
punctuation_marks = [".", ",", "?", "!", ";", ":", "(", ")"]
for i in range(len(punctuation_marks)):
    source = source.replace(punctuation_marks[i], "")
source = source.lower()
words = source.split()
```

Depending on the source text, you might want to do even more cleaning up: removing particular words, for example, or additional punctuation. You'll have to see what comes out in the output and figure out how to best eliminate what you don't want to work with.

What we have here is a potentially very interesting collection of words. Right away, we could create some free verse poetry:

```py
from random import choice

source = open("LC.txt").read()
punctuation_marks = [".", ",", "?", "!", ";", ":", "(", ")"]
for i in range(len(punctuation_marks)):
    source = source.replace(punctuation_marks[i], "")
source = source.lower()
words = source.split()

for j in range(5):      # our poem will have 5 lines

    selections = []
    for i in range(5):  # each line has 5 words
        word = choice(words)
        selections.append(word)
    line = " ".join(selections)
    print(line)
```
```
its hunting three his miles
drudgery tobacco of would and
some from by the on
dry willow it a three
back that eight but is
```

Pretty abstract, but this random collection of words does some sense of the source material. And, of course, each time we run the script, we'll get a new combination.

However, it would be better if there weren't so many common words like "by", or "on", or "it" in there—not that these aren't useful words, but in the interest of poetry, we may do better without them.

Those common words are called "stop words." To filter them out, we'll need a list of them, which you can download here:
- [list_stop_words.txt](list_stop_words.txt)

Once you've downloaded this file, add it to your sketch just like you do for your source text. Because this files is guaranteed to be "clean", we don't have to worry about processing it in any way, and we can condense the code to load it into one line, like this:

```py
stop_words = open("list_stop_words.txt").read().split()
```

Next, we'll create a blank list, `good_words`, which we do with an empty pair of brackets. We'll use a `for` loop and iterate through each of the words from the source, check to see if it's a stop word, and if it's not, add it to our `good_words` list:

```py
source = open("LC.txt").read()
punctuation_marks = [".", ",", "?", "!", ";", ":", "(", ")"]
for i in range(len(punctuation_marks)):
    source = source.replace(punctuation_marks[i], "")
source = source.lower()
words = source.split()

stop_words = open("list_stop_words.txt").read().split()
good_words = []
for i in range(len(words)): # run the loop as many times as there are words
    if words[i] not in stop_words:  
        good_words.append(words[i])
```

As a refresher, note how we used this `for` loop. We run it `len(words)` times—once for each word. The temporary variable `i` tells us what number of the loop we're on, and we can use that as an index to the `words` list. `words[i]` thus becomes a different word for each loop—we check if it is in the stop_words list, and append it to `good_words` if it's not. The list `good_words` now contains all the best words used in the text.

So let's add this algorithm to our free-verse poetry generator:
```py
from random import choice

source = open("LC.txt").read()
punctuation_marks = [".", ",", "?", "!", ";", ":", "(", ")"]
for i in range(len(punctuation_marks)):
    source = source.replace(punctuation_marks[i], "")
source = source.lower()
words = source.split()

stop_words = open("list_stop_words.txt").read().split()
good_words = []
for i in range(len(words)): # run the loop as many times as there are words
    if words[i] not in stop_words:  
        good_words.append(words[i])

for j in range(5):      # our poem will have 5 lines

    selections = []
    for i in range(5):  # each line has 5 words
        word = choice(good_words)   # good_words instead of words
        selections.append(word)
    line = " ".join(selections)
    print(line)
```
```
cemented great forks mississippi believe
without anything bilious wind boiled
goose gray sentinel therefore two
however rain westward platte extensive
high extreme missouris woodland feet
```
Much nicer!

Of course, what would be even more useful is to have the part of speech of each of these words: noun, verb, etc. Then we could combine them in more structured ways.

To pull that off, we're going to need more words lists, containing dictionaries of the different types. I've put some together for you, which you can download here:
- [list_adjectives.txt](list_adjectives.txt)
- [list_interjections.txt](list_interjections.txt)
- [list_nouns.txt](list_nouns.txt)
- [list_prepositions.txt](list_prepositions.txt)
- [list_pronouns.txt](list_pronouns.txt)
- [list_verbs.txt](list_verbs.txt)

By comparing the words of our source text with the words in these lists, we can separate them into parts of speech.

```py
from random import choice

noun_list = open("list_nouns.txt").read().split()
verb_list = open("list_verbs.txt").read().split()
adjective_list = open("list_adjectives.txt").read().split()
preposition_list = open("list_prepositions.txt").read().split()
print("Loaded lists")

source = open("LC.txt").read()
punctuation_marks = [".", ",", "?", "!", ";", ":", "(", ")"]
for i in range(len(punctuation_marks)):
    source = source.replace(punctuation_marks[i], "")
source = source.lower()
words = source.split()
words = list(set(words)) # making them unique, but not bothering with a separate variable
words = words[:1000]
print("Loaded source text")

stop_words = open("list_stop_words.txt").read().split()
good_words = []
for i in range(len(words)): # run the loop as many times as there are words
    if words[i] not in stop_words:  
        good_words.append(words[i])
print("Filtered good words")

nouns = []
verbs = []
adjectives = []
prepositions = []
for i in range(len(good_words)):
    print(i)
    word = good_words[i]
    if word in noun_list:
        nouns.append(word)
    if word in verb_list:
        verbs.append(word)
    if word in adjective_list:
        adjectives.append(word)
    if word in preposition_list:
        prepositions.append(word)
```

Notice that we're using `in` here to determine membership in a list, not a string—`in` works with either.

### Slow code? Take a portion of the text

Also note that this is not a particularly efficient algorithm, so if your text is really long (like "LC.txt" is), it's going to take awhile. That's why I included some `print()` statements in the code—so I know what is going on. If it's too much, use a shorter text, or perhaps just a portion of your text. One approach might be to figure out your algorithm with a short text, and then when its working, apply it to something longer.

We won't go into this syntax in depth, but a way that you can take just the first 1,000 words is like this:
```py
words = words[:1000]
```
That's what I've done above in order to make things a bit more manageable. Using only unique words will cut down on the size, but of course, depending on your algorithm, you will lose something of the character of a text if a certain word is used very often.

### Recombination via part-of-speech

In any case, remember how you can concatenate strings together using the `+` operator? This comes in handy here:
```py
for i in range(10):        
    sentence = "The " + choice(adjectives) + " " + choice(nouns) + " " + choice(verbs) + " " + choice(adjectives) + " " + choice(nouns) + "."
    print(sentence)    
```
```
The teal strata snowing good furniture.
The justly seasons presented quietly length.
The official rats leaf something clamber.
The chalk mantle obliging city pursuit.
The international volumes drink tenderest quest.
The inner tails copying preservative port.
The unacceptable turn invites warmly moccasins.
The yesterday fort benefit plain clearing.
The indecent lover considering unacceptable queues.
The nine horseback believing partial faculties.
```

This is more or less "mad libs" using words from the source text. By providing a basic sentence structure, in this case "The [adjective] [noun] [verb] [adjective] [noun].", we've let the computer fill in the rest. Not all the results are good ones, but they get closer to a more concrete meaning.

How could you get it closer? Maybe filtering for verbs that end in "ed" or removing adjectives ending in "ly" could get things making more sense. Whether or not that serves your artistic purposes is up to you.



////


books
wikipedia articles
transcribed audio
legal texts / laws / contracts
movies: scripts, closed-captioning
lyrics
newspaper articles
social media feeds





change the formatting
replace words
rearrange the sentences

make new sentences:
- rearrange the words
- pull out parts of speech

combine two texts:
- interleave lines
- use different parts of speech from each text
- find common words between two texts

poetry:
- free verse poem
- acrostic
-

analysis:
- sort by length of words
- most commonly used words

////


chop it up into sentences
chop it up into words
pull out parts of speech
sort by alphabetical
sort by length
sort by use
replace all occurrences of one specific word

put things back together randomly
construct madlibs

structure:
- free verse poem
- by line length
-

combine two texts
- by line
- by part of speech
- filter one text by another

/

change the formatting
replace words
rearrange the sentences

make new sentences:
- rearrange the words
- pull out parts of speech

combine two texts:
- interleave lines
- use different parts of speech from each text
- find common words between two texts

poetry:
- free verse poem
- acrostic
-

analysis:
- sort by length of words
- most commonly used words
