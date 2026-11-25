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
    count_label.configure(text=f"{len(students)} STUDENTS")

    for item in info_frame.winfo_children():  
        item.destroy()

    ctk.CTkLabel(info_frame, text=heading, font=("Geist Pixel", 26, "bold"), text_color="#686868").pack(anchor="w", padx=10, pady=(5, 10))
    
    for s in student_list:
        p = percent(s)
        # box student data is put in
        card = ctk.CTkFrame(info_frame, fg_color="#FAFAFA", border_width=1, border_color="#EEEEEE", corner_radius=10)
        card.pack(fill="x", padx=12, pady=7)
        # info labels
        ctk.CTkLabel(card, text=s["name"], font=("Geist Pixel", 19, "bold"), text_color="#686868").pack(anchor="w", padx=18, pady=(13, 5))
        ctk.CTkLabel(card, justify="left", font=("Geist Pixel", 14), text_color="#858585",
                     text=(f"Student No : {s['number']}\n"
                           f"Coursework : {sum(s['marks'])}/60\n"
                           f"Exam : {s['exam']}/100\n"
                           f"Percentage : {p:.2f}%\n"
                           f"Grade : {grade(p)}")).pack(anchor="w", padx=18, pady=(0, 13))

    if footer:
        ctk.CTkLabel(info_frame, text=footer, font=("Geist Pixel", 16), text_color="#686868").pack(anchor="w", padx=10, pady=10)

    info_frame._parent_canvas.yview_moveto(0)  

def view_all():
    if students:
        average = sum(percent(student) for student in students) / len(students)
        preview("All Students", students, f"AVERAGE: {average:.2f}%")

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
        preview("STUDENT RECORD", [student])

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
    average = sum(percent(student) for student in students) / len(students)
    students.sort(key=percent, reverse=descending)
    preview("Highest First" if descending else "Lowest First", students, f"AVERAGE: {average:.2f}%")
    descending = not descending 
    sort_swap.configure(text="Sort ↑" if descending else "Sort ↓")

def save():
    edit_file()
    view_all()

def add():
    number = simpledialog.askinteger("Add Student", "Student number (1000 - 9999):", minvalue=1000, maxvalue=9999)
    if number is None:
        return
    if any(s["number"] == number for s in students):
        messagebox.showerror("Error", f"Student number {number} already exists")
        return

    name = simpledialog.askstring("Add Student", "Full name:")
    if not name or not name.strip():
        return

    mark1 = simpledialog.askinteger("Add Student", "CW 1 (0 - 20):", minvalue=0, maxvalue=20)
    if mark1 is None:
        return
    mark2 = simpledialog.askinteger("Add Student", "CW 2 (0 - 20):", minvalue=0, maxvalue=20)
    if mark2 is None:
        return
    mark3 = simpledialog.askinteger("Add Student", "cW 3 (0 - 20):", minvalue=0, maxvalue=20)
    if mark3 is None:
        return

    exam = simpledialog.askinteger("Add Student", "Exam (0 - 100):", minvalue=0, maxvalue=100)
    if exam is None:
        return

    students.append({"number": number, "name": name.strip(), "marks": [mark1, mark2, mark3], "exam": exam})
    save()

def update():
    student = find()
    if not student:
        return

    number = simpledialog.askinteger("Update Student", "Student number (1000 - 9999):", minvalue=1000, maxvalue=9999)
    if number is None:
        return

    name = simpledialog.askstring("Update Student", "Full name:", initialvalue=student["name"])
    if not name or not name.strip():
        return

    mark1 = simpledialog.askinteger("Update Student", "CW 1 (0 - 20):", initialvalue=student["marks"][0], minvalue=0, maxvalue=20)
    if mark1 is None:
        return
    mark2 = simpledialog.askinteger("Update Student", "CW 2 (0 - 20):", initialvalue=student["marks"][1], minvalue=0, maxvalue=20)
    if mark2 is None:
        return
    mark3 = simpledialog.askinteger("Update Student", "CW 3 (0 - 20):", initialvalue=student["marks"][2], minvalue=0, maxvalue=20)
    if mark3 is None:
        return

    exam = simpledialog.askinteger("Update Student", "Exam (0 - 100):", initialvalue=student["exam"], minvalue=0, maxvalue=100)
    if exam is None:
        return

    student["number"] = number
    student["name"] = name.strip()
    student["marks"] = [mark1, mark2, mark3]
    student["exam"] = exam
    save()

def delete():
    student = find()
    if student and messagebox.askyesno("Delete", f"Delete {student['name']}?"):
        students.remove(student)
        save()

# window
root = ctk.CTk()
root.title("Student Management System")

root.geometry("760x560")
root.resizable(False,False)
root.configure(fg_color="#F4F4F4")

# header + title

header = ctk.CTkFrame(root, fg_color="#F0F0F0", corner_radius=12)
header.pack(side="top", fill="x", padx=20, pady=(20,10))

title = ctk.CTkLabel(header, text="Student Management System", font=("Geist Pixel", 25, "bold"), text_color="#686868")
title.pack(side="left", padx=12, pady=12)

# student count label

count_label = ctk.CTkLabel(header, text="", font=("Geist Pixel", 14), text_color="#888888")
count_label.pack(side="right", padx=12)

# side pannel button holder

sidebar = ctk.CTkFrame(root, fg_color="#FFFFFF", corner_radius=12, border_width=1, border_color="#E5E5E5", width=165)
sidebar.pack(side="left", fill="y", padx=(20,10), pady=10)
sidebar.pack_propagate(False)

ctk.CTkLabel(sidebar, text="MENU", font=("Geist Pixel", 14, "bold"), text_color="#AAAAAA").pack(anchor="w", padx=15, pady=(20,10))

# buh tons

ctk.CTkButton(sidebar, text="View All", command=view_all, font=("Geist Pixel", 14), text_color="#666666", fg_color="#F2F2F2", hover_color="#E5E5E5", corner_radius=8, height=40).pack(fill="x", padx=12, pady=5)
ctk.CTkButton(sidebar, text="View One", command=view_one, font=("Geist Pixel", 14), text_color="#666666", fg_color="#F2F2F2", hover_color="#E5E5E5", corner_radius=8, height=40).pack(fill="x", padx=12, pady=5)
ctk.CTkButton(sidebar, text="Highest", command=highest, font=("Geist Pixel", 14), text_color="#666666", fg_color="#F2F2F2", hover_color="#E5E5E5", corner_radius=8, height=40).pack(fill="x", padx=12, pady=5)
ctk.CTkButton(sidebar, text="Lowest", command=lowest, font=("Geist Pixel", 14), text_color="#666666", fg_color="#F2F2F2", hover_color="#E5E5E5", corner_radius=8, height=40).pack(fill="x", padx=12, pady=5)

ctk.CTkLabel(sidebar, text="-----------------------", font=("Geist Pixel", 14, "bold"), text_color="#AAAAAA").pack(anchor="w", padx=15, pady=(5,5))

# extension

ctk.CTkButton(sidebar, text="Add", command=add, font=("Geist Pixel", 14), text_color="#666666", fg_color="#F2F2F2", hover_color="#E5E5E5", corner_radius=8, height=40).pack(fill="x", padx=12, pady=5)
ctk.CTkButton(sidebar, text="Delete", command=delete, font=("Geist Pixel", 14), text_color="#666666", fg_color="#F2F2F2", hover_color="#E5E5E5", corner_radius=8, height=40).pack(fill="x", padx=12, pady=5)
ctk.CTkButton(sidebar, text="Update", command=update, font=("Geist Pixel", 14), text_color="#666666", fg_color="#F2F2F2", hover_color="#E5E5E5", corner_radius=8, height=40).pack(fill="x", padx=12, pady=5)

sort_swap = ctk.CTkButton(sidebar, text="Sort ↑", command=sort, font=("Geist", 14), text_color="#666666", fg_color="#EAEAEA", hover_color="#DEDEDE", corner_radius=8, height=40)
sort_swap.pack(fill="x", padx=12, pady=(25,10))

# main info frame 

info_frame = ctk.CTkScrollableFrame(root, fg_color="#FFFFFF", corner_radius=12, border_width=1, border_color="#E5E5E5")
info_frame.pack(side="right", fill="both", expand=True, padx=(0,20), pady=10)

read_file()
view_all()
root.mainloop()