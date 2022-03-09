## Sketch #5: Recombination

Choose one or more source texts—newspaper articles, poems, books, lyrics, emails, manifestos, etc—and write a program that recombines its contents to create a new text. The way in which the text is transformed should have an artistic purpose, whether that is to critically comment on the content of your source, explore some formal property of its language, or elicit a particular mood in your audience.

Along with your code and [3-sentence description](../../resources/description_guidelines.md), you should supply an example of your program's output by copying and pasting from the console into a Google Doc. Resist the urge to edit the output to smooth over rough edges; looking back, those often become the most interesting features.

### Resources
- [Recombination context](context.md)
- [Getting started with word_tools](getting_started.md)
- [Coding with recombination](code.md)


### Recombination functions
```py
# loading external text
load_string_from_txt(filename)
load_lines_from_txt(filename)
load_lines_from_srt(filename)

# working with strings of text
get_string_after(text, search)
get_string_before(text, search)
replace_in_string(text, find, replace)
remove_from_string(text, find)

# working with lists
split_into_words(text)
len(string)
sort_list_alpha(list)
sort_list_length(list)
reverse_list(list)
randomize_list(list)
recombine_list(list)
choice(list)

# filtering lists of words and sentences
filter_unique(list)
filter_starts_with(list, s)
filter_ends_with(list, s)
filter_contains(list, s)
filter_nouns(list of words)
filter_singular_nouns(list of words)
filter_plural_nouns(list of words)
filter_verbs(list of words)
filter_imperative_verbs(list of words)
filter_past_tense_verbs(list of words)
filter_present_tense_verbs(list of words)
filter_adjectives(list of words)
filter_pronouns(list of words)
filter_prepositions(list of words)
filter_interjections(list of words)
filter_distinctive(list of words)

# other
count_syllables(word)

# writing to a file
write_string_to_file(text, filename)
```

### Possible sources
- books
- wikipedia articles
- transcribed audio
- legal texts / laws / contracts
- movies: scripts, closed-captioning
- lyrics
- newspaper articles
- social media feeds
