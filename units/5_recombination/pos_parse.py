#!/usr/bin/env python3

"""
c: conjunction or preposition
i: interjection
p: pronoun
s: spoken contraction
n: noun
a: adjective or adverb
"""

outputs = {"list_nouns.txt": "N", "list_verbs.txt": "V", "list_adjectives.txt": "A", "list_prepositions.txt": "C", "list_pronouns.txt": "P", "list_interjections.txt": "I"}

for filename, label in outputs.items():
    with open(filename, 'w') as output:
        with open("pos_raw.txt") as f:
            previous_word = None
            for line in f:
                line = line.strip()
                if line[0] == "-":
                    continue
                tokens = line.split()
                pos = tokens[1].replace(":", "")
                if pos != label:
                    continue
                words = [tokens[0]] + tokens[2:]
                words = [word.replace("(", "").replace(")", "") for word in words]
                words = [word.replace("+", "").replace("!", "") for word in words if word[0] not in ["~", "-", "/", "|", "{"]]
                for word in words:
                    print(word, pos.lower())
                    output.write(word + "\n")
