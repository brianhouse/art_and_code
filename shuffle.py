#!/usr/bin/env python3

import random
from pprint import pprint

students = [line.strip() for line in open('student_list.txt')]
random.shuffle(students)

n = 4
groups = [students[i * n:(i + 1) * n] for i in range((len(students) + n - 1) // n )]  


pprint(groups)