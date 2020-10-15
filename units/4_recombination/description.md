## Concept

Digital media are always composed of discrete elements—from 1s and 0s on the most fundamental level of digital representation, to the characters of text or the samples of audio, to the files and folders that comprise an operating system. Though these elements are always of a finite number, it is the way that they can be combined and recombined that results in (practically) limitless possibilities.

Of course, this property is also intrinsic to non-electronic systems—most notably, perhaps, the alphabet, through which the expressive potential of entire cultures is produced through the reordering of letters (just 26 in the case of English). But digital media excel at enumerating through all of the possibilities and finding ones that we might never have otherwise come up with. Like with nonlinear narrative, this property of recombination tasks the artist-programmer with designing a system for generating all potential versions, rather than only one particular version, and letting the computer plumb its limits.

## Context

### Non-digital

Practices by avant-garde artists and poets have prefigured some of the combinatory powers of computers, particularly when it comes to manipulating language. Just like with indeterminacy in visual art, the Dadaists applied their scissors and chance-based operations to words:

<p align="center">
  <img src="context/1_tzara.png" width=400 /><br />
  Tristan Tzara, "To Make a Dadist Poem" (1920)
</p>

This "cut-up" technique was popularized in the mid-20th century by the well-known beat poet and provocateur [William S. Burroughs](https://en.wikipedia.org/wiki/William_S._Burroughs) (1914–1997), together with his friend, artist Brion Gysin (1916–1986). Burroughs' novel _The Soft Machine_ (1961), for example, was entirely constructed of a different text, _The Word Hoard_, that Burroughs had written in the years prior. Burroughs sliced up the earlier text and rearranged it to create the new novel, suggesting that the process helped reveal the "true meaning" of the original.

<p align="center">
  <img src="context/2_burroughs.jpg" width=400 /><br />
  William S. Burroughs, pieces of <i>The Word Hoard</i> (1954–1958)
</p>

Subsequently, Burroughs' influence on the counter-culture led to the cut-up technique being used by artists from punk writer [Kathy Acker](https://en.wikipedia.org/wiki/Kathy_Acker) (_Blood and Guts in High School_ (1978)) to Thom Yorke of Radiohead, who pulled lyrics out of a hat for the album [_Kid A_](https://en.wikipedia.org/wiki/Kid_A) (2000). Experimental turntablist DJ Spooky, That Subliminal Kid takes his name from a Burroughs character and has [theorized the parallels](https://theinfluencers.org/en/dj-spooky) between the cut-up technique and DJ culture.

<p align="center">
  <img src="context/3_dj_spooky.jpg" width=400 /><br />
  DJ Spooky performing in 2013
</p>

The French literary group Oulipo (founded in 1960) is also notable for exploring combinatoric logic in their writing. "Oulipo" is short for the French for "workshop of potential literature" and the group blurs the lines between poetry and puzzle in their pieces. For example, Georges Perec used a "story-making machine" in which the narrative is guided by [algorithmic combinations of people, feelings, and objects](http://tselfoninternets.blogspot.com/2010/04/stuff.html) for his novel [_Life: A User's Manual_](https://en.wikipedia.org/wiki/Life:_A_User%27s_Manual) (1978); for _A Void_ (1969) he wrote a 300-page book that does not contain the letter "e."

However, the work that perhaps most directly expresses the spirit of the Oulipo is Raymond Queneau's _A Hundred Thousand Billion Poems_ (1961).

<p align="center">
  <img src="context/4_queneau.png" width=400 /><br />
  The sliced pages of Raymond Queneau's <i>A Hundred Thousand Billion Poems</i> (1961) — watch <a href="https://www.youtube.com/watch?v=2NhFoSFNQMQ">here</a>.
</p>

The work consists of 10 [sonnets](https://en.wikipedia.org/wiki/Sonnet) with the same rhyme pattern, with the pages of each sonnet cut between each of their 14 lines. By manually flipping each of the resulting strips, each of the 10 possibilities for each line can be combined with any other, yielding 100,000,000,000,000 (10^14) possible poems. Part of the brilliance of this piece is that if you choose a particular poem and read it, you are likely to be the only person ever to read that poem.


### Digital

Text can be manipulated by code in ways reminiscent of the cut-up technique or the Oulipo strategies, albeit with somewhat less mess.

One example comes from pop musician and cultural icon [David Bowie](https://en.wikipedia.org/wiki/David_Bowie). In the 1990s, Bowie and collaborator Ty Roberts created the [Verbasizer](https://www.vice.com/en_us/article/xygxpn/the-verbasizer-was-david-bowies-1995-lyric-writing-mac-app), which automizes the cut-up technique to produce lyrics. Bowie: "what you end up with is a real kaleidoscope of meanings and topic and nouns and verbs all sort of slamming into each other."

<p align="center">
  <img src="context/5_bowie.png" width=400 /><br />
  Bowie using the Verbasizer.
</p>

Taking things a step further, the digital media artist [Allison Parrish](https://www.decontextualize.com) is known for her work creating algorithmic literature. Her book _Our Arrival_ (2015) for instance, draws source material from [Project Gutenberg](https://www.gutenberg.org), a collection of novels in the public domain. Parrish selects and recombines sentences from this source according to a set of criteria that make it a meditation on the natural world.

Taking things online, Darius Kazemi applies some of the same techniques toward the construction of [Twitter bots](https://en.wikipedia.org/wiki/Twitter_bot). Whereas bots are often a hazard of disinformation online, Kazemi's bots are alternately clever, poignant, or sarcastic, such as [Roof Slapping Bot](https://twitter.com/RoofSlappingBot) or [Which One Bot](https://twitter.com/WhichOneBot) which combine phrases found from various online sources.

One final piece uses some basic text analysis to produce a kind of data visualization: Luke DuBois' [_Hindsight is Always 20/20_](https://learninglab.si.edu/collections/hindsight-is-always-20-20/p7A3AxJofG9Uy4mT) takes the State of the Union addresses from each US President and arranges them on a traditional eye chart according to the most commonly used words:

<p align="center">
  <img src="context/6_dubois_lincoln.jpg" width=400 /><br />
  <i>Hindsight is Always 20/20</i>: Abraham Lincoln
</p>

<p align="center">
  <img src="context/6_dubois_bush.jpg" width=400 /><br />
  <i>Hindsight is Always 20/20</i>: George W. Bush
</p>

## Code: language machines

We've already learned how to use variables to store single strings. To do more complicated manipulation of text, however, we'll need additional structures that can store more than one thing at a time. In Python, these are called *lists* (in other programming languages, they are frequently called arrays). Lists can be generated within a program, but they can also be a means of storing data loaded from external sources. Together with strings, conditional logic, and for loops, lists open up new possibilities

For this code, please begin by downloading [this template](recombination_sketch.zip) (click the "download" button after following this link), which includes additional functions and libraries. Although we will continue to work with text, we will be working in the Processing app, not in the terminal.


### Strings and lists


Consider the following string:

```py
sentence = "I find this piece to be a great example of art."
```

We also know that variables that are strings have certain built-in capabilities; for example, we know that `sentence.lower()` will make all of the characters in the string lowercase. Functions like this that are attached to objects—ie, they come after a dot—are called **methods**.

Another example of a string method is `.split()`:

```py
sentence = "I find this piece to be a great example of art."
words = sentence.split()
print(words)
```
...which will produce this in the console:
```py
['I', 'find', 'this', 'piece', 'to', 'be', 'a', 'great', 'example', 'of', 'art.']
```

As you can see, `split()` has divided the string at every space. This results in a new structure, delineated by `[` and `]` which is a **list**.

A list is a very powerful kind of variable—it's actually more of a meta-variable, because it holds a sequence of other things. These might be numbers, booleans (aka `True`/`False`), strings, or other objects. This list, `words`, currently has 11 items in it, all of them different strings.

We can access items in lists using square brackets and an index number after the list variable name. For example, `words[0]` is the string "I", `words[1]` is the string "find", `words[2]` is the string "this", and so forth.

(Why do lists start with index 0 instead of 1? They just do, and ultimately it is easier this way, although it takes some getting used to.)

Using brackets and index numbers, we can change the value of one of the items in the list:

```py
sentence = "I find this piece to be a great example of art."
words = sentence.split()
words[7] = "questionable"
print(words)
```
```py
['I', 'find', 'this', 'piece', 'to', 'be', 'a', 'questionable', 'example', 'of', 'art.']
```
There's another string method, `join()`, which puts the sentence back together. Awkwardly, however, `join()` is a method of the separator character, and it takes the list as a parameter:
```py
sentence = "I find this piece to be a great example of art."
words = sentence.split()
words[7] = "questionable"
sentence = " ".join(words)  # use a space to join words
print(sentence)
```
```py
I find this piece to be a questionable example of art.
```

Using `split()`, indexes, and `join()`, we've now taken apart a sentence, swapped out a word, and put it back together again.

### Word replacement with loaded lists

Lists can be used for many different things—including loading data from files. For example, included in the template folder for this assignment is a file that contains a list of _isms_. That's right—the names of conceptual art movements and so forth. We can load it like this:

```py
isms = open("isms.txt").read().splitlines()
```
This sequence of methods reads "isms.txt" into memory and splits all of the lines into separate items of a list (try printing it to the console to see).

To randomly select an ism, we'll need a new function—`choice()`. This doesn't come enabled by default, so we have to include a special line at the beginning of our program:

```py
from random import choice   # enables the choice function

isms = open("isms.txt").read().splitlines()

an_ism = choice(isms)
print(an_ism)
```
```
neo-impressionism
```

Returning to our previous example, we can now start to make things more interesting:

```py
from random import choice

isms = open("isms.txt").read().splitlines()

sentence = "I find this piece to be a great example of art."
words = sentence.split()
words[10] = choice(isms) + "."
sentence = " ".join(words)  # use a space to join words
print(sentence)
```
```py
I find this piece to be a great example of dadaism.
```

With another word list loaded from a text file, adjectives, we can take things further:
```py
from random import choice

adjectives = open("adjectives.txt").read().splitlines()
isms = open("isms.txt").read().splitlines()

sentence = "I find this piece to be a great example of art."
words = sentence.split()
words[7] = choice(adjectives)
words[10] = choice(isms) + "."
sentence = " ".join(words)  # use a space to join words
print(sentence)
```
```py
I find this piece to be a cluttered example of neue slowenische kunst.
```

Might as well fill out the review:

```py
from random import choice

adjectives = open("adjectives.txt").read().splitlines()
adverbs = open("adverbs.txt").read().splitlines()
nouns = open("nouns.txt").read().splitlines()
isms = open("isms.txt").read().splitlines()

# make multi-line strings with triple-quotes
sentence = """
            I find this piece to be a great example of art.
            The lines are straight and the colors seem dull.
            It is, frankly, a normal painting.
            """
words = sentence.split()
words[7] = choice(adjectives)
words[10] = choice(isms) + "." # add a period
words[14] = choice(adjectives)
words[18] = choice(adverbs)
words[19] = choice(nouns) + "."
words[24] = choice(adjectives)
words[25] = choice(nouns) + "."
sentence = " ".join(words)  # use a space to join words
print(sentence)
```
```
I find this piece to be a grubby example of cubo-futurism.
The lines are sweaty and the colors shakily stay.
It is, frankly, a secondary hippopotamus.   
```
Ok, well, it's not perfect. But using a little rudimentary grammar, some word lists, and substituting for a template, we get a pretty interesting critique. Or rather, as many critiques as we could ever want (consider how you might use a `for` loop to accomplish this).

BTW, the word lists included in the template are:

```
adjectives.txt
adverbs.txt
animals.txt
body_parts.txt
celebrities.txt
cities.txt
isms.txt
jobs.txt
moods.txt
nouns.txt
objects.txt
prepositions.txt
stop_words.txt
verbs_infinitive.txt
verbs_past.txt
verbs_present.txt
```

These files are in the "data" folder inside the sketch folder, and you can look at their contents and format by opening them directly. To add your own, you can either just put a file into the data folder, or use the "Add File" option in Processing:


<p align="center">
  <img src="code/1_add_file.png" width=200 />
</p>

You can subsequently load the file in the same way using the name of the file as a string parameter to Python's `open` command (eg, "adverbs.txt"). Note that only plain text files will work (no Word files), and the words have to be one per line to convert directly to a list.


### Cut-ups with loaded text

Loading data from external files is powerful, but we aren't limited to just using curated lists of words. In fact, we might load whole preexisting texts. For example, we can download a book in "Plain Text" format from the [Gutenberg Project](https://www.gutenberg.org), such as [_History of the Expedition under the Command of Captains Lewis and Clark, Vol. I._](https://www.gutenberg.org/ebooks/16565). I've saved this text file from the browser on my desktop, changed the filename to "lc_expedition.txt", and added it to my sketch with "Add File...".

```py
source = open("lc_expedition.txt").read()    # not using .splitlines() this time
```

The variable `source` now contains the complete text—an enormous string (we leave off `.splitlines()` because this would turn it into a list of words, which we don't want (yet)).

To make our lives simpler down the road, before we do anything else, we're going to clean the text up a bit. We'll use a trick to do this, which is to `.split()` the string on all whitespace characters (spaces, line breaks, tabs, etc), and then immediately put it back together again with `.join()`. This will have the effect of collapsing everything into sentences without additional formatting.

```py
source = open("lc_expedition.txt").read()
source = " ".join(source.split()) # clean up whitespace
```

Now that we've cleaned the text, we're ready to reproduce the cut-up technique. To start off, instead of splitting it into individual words, let's start with individual sentences:

```py
source = open("lc_expedition.txt").read()
source = " ".join(source.split())
sentences = source.split(". ")    # use a parameter with split
```

We gave `.split()` a parameter, ". ", to tell it to break not on any whitespace, but on periods followed by spaces. As a result, `sentences` is now a list of sentences. How many? `len()` will tell us:

```py
source = open("lc_expedition.txt").read()
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

source = open("lc_expedition.txt").read()
source = " ".join(source.split())
sentences = source.split(".")

random_sentence = choice(sentences)
print(random_sentence)

```
```
 we are much pleased in finding him by no means as ill as we had expected
```

To create a cut-up, we want to take several random sentences and piece them together to form a new text. To do that, we're going to start with an empty list (we'll call it `cut_up`), which in Python you make like this:
```py
cut_up = []
```
To add items to a list, we use the `.append()` method. Combined with a `for` loop, we can use it to pull 5 random sentences from the expedition:

```py
from random import choice

source = open("lc_expedition.txt").read()
source = " ".join(source.split())
sentences = source.split(". ")

cut_up = []
for i in range(5):
    cut_up.append(choice(sentences))

output = ". ".join(cut_up)    
output = output + "."   # add a final period
print(output)
```

On each iteration of the loop, the program chooses a random item from the `sentences` list and appends it to the `cut_up` list. Using `join()`, this time with a period in addition to a space, we paste the sentences back together. `output` is now the new string:

```
The morning was fine, and three men were despatched ahead to hunt, while the rest were detained until nine o'clock, in order to retake some horses which had strayed away during the night. The road was still difficult, and several of the horses fell and injured themselves very much, so that we were unable to advance more than ten miles to a small stream, on which we encamped. Sunday, December 2. If therefore you intend to keep your promise, send one of the young men immediately to order the people to remain at the village till we arrive. The country, generally, consists of low, rich, timbered ground on the north, and high barren lands on the south: on both sides great numbers of buffaloe are feeding.
```

While the result is not exactly linearly coherent, we do indeed get a sense of the tenor of the text. To add a little twist, let's substitute some words using the `.replace()` method. This method takes two parameters: the string to search for, and the string to replace it with.

```py
output = output.replace("men", "spacemen")
output = output.replace("encampment", "space station")
output = output.replace("miles", "light-years")
output = output.replace("feet", "rocket boosters")
output = output.replace("party", "crew")
output = output.replace("skins", "spacesuits")
output = output.replace("hail", "solar flare")
```
```
The morning is clear and cold, the mercury at sunrise 22° below 0. The spacemen complain much of the bruises received yesterday from the solar flare. During his absence the crew had been occupied in dressing spacesuits, and being able to rest themselves were nearly freed from their lameness and swollen rocket boosters. They leave their space station, and proceed on their journey. We had a breeze from the southeast, and made thirteen light-years.
```

Perhaps a contrived example, but clever word substitution can reframe the context of a text (imagine what you could do with a newspaper article, for example).


### Collecting words and counting syllables

A source text can also be used to provide a vocabulary for new works. Rather than using the cut-up technique on the level of sentences, we can clean and divide the text on the level of words.

This time, after we load our text, we first convert everything to lowercase and remove all punctuation (we'll have to import a special function for that). Then we split it into words:

```py
from word_helper import remove_punctuation # import the remove_punctuation

source = open("lc_expedition.txt").read()
source = source.lower()
source = remove_punctuation(source)
words = source.split()
```

This is a potentially very interesting collection of words. However, a lot of these words will be very commonly used words in English. For the sake of poetry, it would be nice to keep just the most interesting ones, the ones that make the character of the source what it is.

Those common words are called "stop words," and we can filter them out. First, we'll need to load a word list, which we have:

```py
from word_helper import remove_punctuation # import the remove_punctuation

source = open("lc_expedition.txt").read()
source = source.lower()
source = remove_punctuation(source)
words = source.split()

stop_words = open("stop_words.txt").read().splitlines() # split into a list
```

Next, we'll create a blank list, `good_words`, which we do with an empty pair of brackets. We'll use a `for` loop and iterate through each of the words from the source, check to see if it's a stop word, and if it's not, add it to our `good_words` list:

```py
from word_helper import remove_punctuation # import the remove_punctuation function

source = open("lc_expedition.txt").read()
source = source.lower()
source = remove_punctuation(source)
words = source.split()

stop_words = open("stop_words.txt").read().splitlines() # split into a list
good_words = []
for i in range(len(words)): # run the loop as many times as there are words
    if words[i] not in stop_words:  
        good_words.append(words[i])
```

Note how we used this `for` loop. We run it `len(words)` times—once for each word. The temporary variable `i` tells us what number of the loop we're on, and we can use that as an index to the `words` list. `words[i]` thus becomes a different word for each loop—we check if it is in the stop_words list, and append it to `good_words` if it's not.

The list `words` now contains all the best words used in the text. Since these words previously combined to form a very long narrative, what if we used them for something entirely different?

[Haiku](https://en.wikipedia.org/wiki/Haiku) is a traditional form of poetry from Japan. Each poem consists of just three lines, of 5, 7, and 5 syllables, respectively.

To make haikus from the vocabulary of the Lewis and Clark expedition, we're going to need to import another function, `count_syllables`. We're also going to use another variation on random, which is `shuffle`.

The general idea here is that first we'll shuffle our `good_words` list into a random order. Then, for line one of the haiku, we'll pull out the first combination of words that adds up to 5 syllables. Look at the code annotations for how this works.

```py
# import functions
from word_helper import remove_punctuation
from word_helper import count_syllables # import the count_syllables function
from random import shuffle

# load source words
source = open("lc_expedition.txt").read()
source = source.lower()
source = remove_punctuation(source)
words = source.split()

# filter out stop_words
stop_words = open("stop_words.txt").read().splitlines()
good_words = []
for i in range(len(words)):
    if words[i] not in stop_words:  
        good_words.append(words[i])

# shuffle the good words into a random order
shuffle(good_words)

line_1 = []                         # create an empty list for line 1
remaining_syllables = 5              # use a variable to keep track of the syllables we have left
for i in range(len(good_words)):    # loop through the good words
    syllables = count_syllables(good_words[i])    # count the syllables of a word
    # this returns None if it doesn't recognize the word
    if syllables is not None and syllables <= remaining_syllables:    # check if the syllables are less than or equal to the ones we need
        line_1.append(good_words[i])        # if so, append the word to line 1
        remaining_syllables = remaining_syllables - syllables   # subtract the syllables of this word from those remaining
    if remaining_syllables == 0:    # if we have all our syllables...
        break                       # break out of the loop.
print(" ".join(line_1))             # finally, join the list together and print it
```
```
little hills ears glass
```
This example is somewhat complex, as it uses `if` and `for` together with lists, and keeps track of its progress with variables. This code just completes the first line of the poem, but for lines two and three, we can just shuffle `good_words` again and repeat a similar block of code to make a `line_2` list, starting with 7 remaining syllables. Likewise for final line.

Some results:
```
destroys mountains bend
deer proceeded party chief
mountains soon pointed
```
```
recede round hand strayed
miles vast whose bear winter yards
cottonwood viewed rain
```
```
covered river earth
red remain side whole returned
timber till purple
```

Despite coming from a machine, we can read some poignancy in the lines that expresses something of the Romantic ideals and colonial reality that was the expedition.


### Bonus: rhymes

Since we're talking about poetry, we need to include some rhymes.

```py
from random import choice

jobs = open("jobs.txt").read().splitlines()
cities = open("cities.txt").read().splitlines()
verbs_past = open("verbs_past.txt").read().splitlines()
nouns = open("nouns.txt").read().splitlines()

job = choice(jobs)
city = choice(cities)

line_1 = "There once was a " + job + " from " + city
print(line_1)
```
```
There once was a credit checker from Hartford
```

For the second line of the poem, the last word has to rhyme with the city. We can use the `rhymes` function, which returns a list, to find possible rhymes, and choose randomly from those.

```py
from random import choice
from word_helper import rhymes  # import rhymes function

jobs = open("jobs.txt").read().splitlines()
cities = open("cities.txt").read().splitlines()
verbs_past = open("verbs_past.txt").read().splitlines()
nouns = open("nouns.txt").read().splitlines()

job = choice(jobs)
city = choice(cities)

line_1 = "There once was a " + job + " from " + city
print(line_1)

rhyming_word = choice(rhymes(city))
line_2 = "Who " + choice(verbs_past) + " with a " + choice(adjectives) + " " + rhyming_word
print(line_2)
```
```
There once was a executive secretary from Scottsdale
Who irritated with a hilarious gmail
```

This doesn't always work and isn't often very good, but you get the idea.


## Sketch #4

This sketch will consist of a language machine that outputs variations of some sort of structured text via recombination. The exact form that it takes is up to you. You might take a form of poetry, such as a sonnet or free verse, and create variations by using random words from the provided lists or ones you curate. You could also remix a famous art manifesto or political statement, rewrite a newspaper article with substituted words, auto-generate rap lyrics, or produce alternative closed captions for a film. Challenge yourself to produce a novel algorithm that doesn't replicate the examples.

Along with your code and [3-sentence description](../../resources/description_guidelines.md), you should supply three versions of your text output (that result from identical code!) so we can see the nature of the variation that your program produces. Resist the urge to edit the output to smooth over rough edges; looking back, those often become the most interesting features.
