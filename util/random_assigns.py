#!/usr/bin/env python3

import json
from random import shuffle, randint

GROUP_SIZE = 4

with open("students.txt") as f:
    students = [line.strip() for line in f.readlines()]

reviewers = students[:]
reviewees = students[:] * GROUP_SIZE

assignments = {}
for reviewer in reviewers:
    assignments[reviewer] = []
    while len(assignments[reviewer]) < GROUP_SIZE and len(reviewees):
        index = randint(0, len(reviewees)-1)
        reviewee = reviewees[index]
        if reviewee != reviewer and reviewee not in assignments[reviewer]:
            assignments[reviewer].append(reviewee)
            del reviewees[index]
    # print(assignments)

for student in assignments:
    print(student, assignments[student])
# print(json.dumps(assignments, indent=4))

print()
for student in students:
    count = 0
    for reviewer in students:
        if student in assignments[reviewer]:
            count += 1
    print(student + " " + str(count))
