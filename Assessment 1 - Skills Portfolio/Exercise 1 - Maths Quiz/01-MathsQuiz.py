# CodeLab II Assessment 1 || 01 Maths Quiz
# Submitted By: Gayl Ragunjan Creative Computing G2 

import tkinter as tk
import random
from tkinter import messagebox

# variables

questions = 10
difficulty = ""
score = 0
answer = 0
count = 0

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
    difficulty_label.config(text=f"{difficulty} Mode / Question #{count}")

# chain of questions

def next_question():
    answer_entry.delete(0, tk.END)
    answer_entry.config(fg="#000000")
    answer_entry.focus()

    make_question()

# checking an answer

def check():
    global score, count

    try:
        guess = int(answer_entry.get())
    except ValueError:
        messagebox.showerror("Nuh Uh!", "not a number!")

        def clear_warning():
            messagebox.showerror("Nuh Uh!", "not a number!")

        answer_entry.after(1200, clear_warning)
        return

    if guess == answer:
        score += 1
    else:
        messagebox.showerror("Nuh Uh!", f"Wrong answer friend... It was {answer}!")

    count += 1

    # score_update.config(text=f"Score: {score}") 

    if count >= questions:
        show_results()
    else:
        next_question()


# results!!!

def show_results():

    if score == 10:
        msg = "Perfect score! Mathematical!!!"
    elif score >= 8:
        msg = "Dang... Almost perfect!"
    elif score >= 5:
        msg = "You can do better!"
    else:
        msg = "Oh Glorb! Gotta practice sum more..."

    # final_score.config(text=f"{score} / 10")

    # congrats_message.config(text=msg)


root = tk.Tk()
root.title("BMO's Maths Quiz!")

root.geometry("250x350")
root.resizable(False, False)

root.configure(bg="#FFFFFF")

random_question = tk.Label(root, text="", font=(18), fg="#05342F")
random_question.pack()

difficulty_label = tk.Label(root, text="", font=(18), fg="#05342F")
difficulty_label.pack()

answer_entry = tk.Entry(root, text="", font=(18), fg="#05342F")
answer_entry.pack()

root.mainloop()
