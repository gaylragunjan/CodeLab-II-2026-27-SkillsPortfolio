# CodeLab II Assessment 1 || 01 Maths Quiz
# Submitted By: Gayl Ragunjan Creative Computing G2 

import tkinter as tk
import random

# variables

questions = 10
difficulty = ""
score = 0
answer = 0

# random numbers

def random_number():
    if difficulty == "Easy":
        return random.randint(0, 99)
    if difficulty == "Medium":
            return random.randint(100, 999)
    if difficulty == "Hard":
            return random.randint(1000, 9999)

# operations 

def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b

operations = {"+": addition, "-": subtraction}

# creating a randomized question

def make_question():
    global answer

    a = random_number()
    b = random_number()
    add_or_subtract = random.choice(list(operations)) 
    answer = operations[add_or_subtract](a, b)

    random_question.config(text=f"{a} {add_or_subtract} {b} = ?")
    difficulty_label.config(text=f"{difficulty} Mode / Question #__")


root = tk.Tk()
root.title("BMO's Maths Quiz!")

root.geometry("250x350")
root.resizable(False, False)

root.configure(bg="#FFFFFF")

random_question = tk.Label(root, text="", font=(18), fg="#05342F")
random_question.pack()

difficulty_label = tk.Label(root, text="", font=(18), fg="#05342F")
difficulty_label.pack()

root.mainloop()