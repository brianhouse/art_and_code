#!/usr/bin/env python3

import json
from random import shuffle, randint
from itertools import combinations

with open("present.txt") as f:
    students = [line.strip() for line in f.readlines()]

shuffle(students)

# results = list(combinations(students, 2))
# for result in results:
#     print(result)

i = 0
while i < len(students):
    print(students[i] + "," , students[i+1])
    i += 2
