import tkinter as tk
import os
import json

main_directory = os.path.dirname(os.path.abspath(__file__))

def path(filename): 
    return os.path.join(main_directory, "Assets", filename)

student_json = path("studentMarks.json")

students = [] # guide : number , name , marks , exam

# open file

def read_file():
    with open(student_json, "r") as f:
        students.extend(json.load(f))

# edit file

def edit_file():
    with open(student_json, "w") as f:
        json.dump(students, f, indent=2)

def student_info(student):
    scores_total = percent(student)
    return (f"{student['name']}\n" f"Student No. : {student['number']}\n" f"Coursework : {sum(student['marks'])}/60  {student['marks']}\n" f"Exam : {student['exam']}/100\n" f"Percentage : {scores_total:.2f}%\n" f"Grade : {grade(scores_total)}\n")

def percent(student):
    return (sum(student["marks"]) + student["exam"]) / 160 * 100

def grade(scores_total):
    if scores_total >= 70:
        return "A"
    elif scores_total >= 60:
            return "B"
    elif scores_total >= 50:
                return "C"
    elif scores_total >= 40:
                return "D"
    else:
        return "F"

students = [
    {"number": 1778, "name": "gayl", "marks": [15, 18, 20], "exam": 80},
    {"number": 1434, "name": "aydee", "marks": [5, 3, 16], "exam": 40},
]

# display 

def preview(heading, student_list=(), footer=""):
    print(heading)
    for student in student_list:
        print(student_info(student))
    if footer:
        print(footer)


print(grade(70), grade(69.98), grade(40), grade(20)) 

preview("All Students", students)

preview("Highest", [max(students, key=percent)])

preview("Lowest", [min(students, key=percent)])