#!/usr/bin/env python3

import yaml, sys, json

F  = 0      # non-existent
B_ = 80     # unsatisfactory - fails to fulfill the basic requirements
B  = 85     # satisfactory - functional / conceptually sound as expected
A_ = 90     # going places, but uneven
A  = 95     # a level of refinement and/or experimentation beyond the basic requirements


## sample student data
student = """
assignments:
    1: A, A     # concept / craft
    2: B, B
    3: B, B
    4: A-, A
    5: A, A
    6: A, A
    7: A, A
    8: B, A
    9: B, B
    10: B,B
presentation: A-
absences: 0
distractions: 0
"""

## load student data
print()
try:
    with open("students/" + sys.argv[1].split('.')[0] + '.yaml') as f:
        print(sys.argv[1].upper().split('.')[0])
        student = yaml.safe_load(f.read())
except IndexError:
    print('[student]')
    print()
    print('EXAMPLE')
    student = yaml.safe_load(student)
except Exception as e:
    print(e)
    exit()


## calculate grade on assignments
assignments = [assignment.replace('-', '_') for assignment in student['assignments'].values()]
assignments = [list(eval(assignment)) for assignment in assignments]
assignment_grade = sum(sum(assignments, [])) / (len(assignments) * 2 * 100)
print(f"This sketch: {assignments[-1][0]} concept / {assignments[-1][1]} craft")
print(f"Sketches to date: {(assignment_grade * 100)}")


## calculate grade on presentation
if 'presentation' in student and student['presentation'] is not None:
    presentation = globals()[student['presentation'].replace('-', '_')]
    print(f"Presentation: {presentation}")
    presentation_grade = presentation / 100
    raw_grade = (assignment_grade * .9) + (presentation_grade * .1)
else:
    raw_grade = assignment_grade


"""
    absence -2.5%, 1 free
    distraction (late or social media use) -1.25%
    capped at -10%
"""
absence_factor = 0
if 'absences' in student and student['absences'] is not None:
    absence_factor = max((student['absences'] - 1), 0) * 0.025
if 'distractions' in student and student['distractions'] is not None:
    absence_factor += student['distractions'] * 0.0125
absence_factor = min(absence_factor, .1)
print(f"Absences and lateness/distractions: -{absence_factor * 100}")
final_grade = raw_grade - absence_factor
final_grade *= 100

print(f"Course to date: {final_grade}")
