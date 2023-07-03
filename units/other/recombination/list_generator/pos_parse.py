#!/usr/bin/env python3

kinds = [   'nouns',
            'nouns_plural',
            'adjectives',
            'prepositions',
            'pronouns',
            'interjections',
            'verbs_imperative',
            'verbs_present',
            'verbs_past',
            ]

files = {}
for kind in kinds:
    files[kind] = open(kind + ".txt", 'w')

with open("pos_raw.txt") as f:
    previous_word = None
    for line in f:
        line = line.strip()
        if line[0] == "-":
            continue
        tokens = line.split()
        pos = tokens[1].replace(":", "")
        root = tokens[0].strip("+")
        subs = [sub for sub in tokens[2:] if sub[0] not in ["~", "-", "/", "|", "{", "("]]
        if pos == "N":
            files['nouns'].write(root + "\n")
            for sub in subs:
                files['nouns_plural'].write(sub + "\n")
        elif pos == "V":
            files['verbs_imperative'].write(root + "\n")
            if len(subs):
                files['verbs_present'].write(subs[-1] + "\n")
            if len(subs) > 1:
                files['verbs_past'].write(subs[0] + "\n")
        elif pos == "A":
            files['adjectives'].write(root + "\n")
        elif pos == "C":
            files['prepositions'].write(root + "\n")
        elif pos == "P":
            files['pronouns'].write(root + "\n")
        elif pos == "I":
            files['interjections'].write(root + "\n")
