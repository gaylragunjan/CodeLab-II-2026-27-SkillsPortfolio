import tkinter as tk
import os
import json
from tkinter import simpledialog, messagebox
import customtkinter as ctk

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

# percent and grade system

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
    
# display 

def preview(heading, student_list=(), footer=""):
    count_label.configure(text=f"{len(students)} students")
    output.configure(state="normal")
    output.delete("1.0", "end")
    output.insert("end", heading + "\n\n")

    for student in student_list:
        p = percent(student)
        output.insert("end", f"{student['name']}\n" f"Student No. : {student['number']}\n" f"Coursework: {sum(student['marks'])}/60 Exam: {student['exam']}/100\n" f"{p:.1f}% Grade {grade(p)}\n\n")

    output.insert("end", footer)
    output.configure(state="disabled")

def view_all():
    if students:
        average = sum(percent(student) for student in students) / len(students)
        preview("All Students", students, f"Average: {average:.2f}%")

# student search 

def find():
    text = simpledialog.askstring("Find", "Name or number:")
    if text is None:
        return None
    for student in students:
        if text.strip().lower() == student["name"].lower() or text.strip() == str(student["number"]):
            return student
    messagebox.showerror("Error", "Student Not in System")
    return None

def view_one():
    student = find()
    if student:
        preview("Student Record", [student])

# display sort

def highest():
    if students:
        preview("Highest", [max(students, key=percent)])

def lowest():
    if students:
        preview("Lowest", [min(students, key=percent)])

descending = True

def sort():
    global descending
    students.sort(key=percent, reverse=descending)
    preview("Highest First" if descending else "Lowest First", students)
    high_first = not descending

# window

root = ctk.CTk()
root.title("Student Management System")

root.geometry("760x560")
root.resizable(False,False)

header = ctk.CTkFrame(root, fg_color="transparent")
header.pack(side="top", fill="x", padx=10, pady=5)

title = ctk.CTkLabel(header, text="Student Management System", font=("Consolas", 20, "bold"))
title.pack(side="left")

count_label = ctk.CTkLabel(header, text="", font=("Consolas", 15))
count_label.pack(side="right")

sidebar = ctk.CTkFrame(root)
sidebar.pack(side="left", fill="y", padx=10, pady=15)

ctk.CTkButton(sidebar, text="View All", command=view_all, font=("Consolas", 14)).pack(padx=10, pady=5)
ctk.CTkButton(sidebar, text="View One", command=view_one, font=("Consolas", 14)).pack(padx=10, pady=5)
ctk.CTkButton(sidebar, text="Highest", command=highest, font=("Consolas", 14)).pack(padx=10, pady=5)
ctk.CTkButton(sidebar, text="Lowest", command=lowest, font=("Consolas", 14)).pack(padx=10, pady=5)
ctk.CTkButton(sidebar, text="Sort", command=sort, font=("Consolas", 14)).pack(padx=10, pady=5)
    
output = ctk.CTkTextbox(root, state="disabled", font=("Consolas", 14))
output.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)

read_file()
view_all()
root.mainloop()