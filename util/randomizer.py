#!/usr/bin/env python3

from random import shuffle

with open("students_present.txt") as f:
    students = [line.strip() for line in f.readlines()]

while True:

    shuffle(students)
    i = 0
    print("-----")

    while True:
        wait = input()
        print(students[i].strip())
        i += 1
        if i == len(students):
            break
