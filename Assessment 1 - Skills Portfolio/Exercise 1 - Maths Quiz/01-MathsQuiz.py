# CodeLab II Assessment 1 || 01 Maths Quiz
# Submitted By: Gayl Ragunjan Creative Computing G2 

import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# variables

questions = 10
difficulty = ""
score = 0
answer = 0
count = 0
attempts = 0

# random numbers

def random_number():
    if difficulty == "Easy":
        return random.randint(0, 9)
    if difficulty == "Medium":
            return random.randint(10, 99)
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
    difficulty_label.config(text=f"{difficulty} - Question #{count}")

# chain of questions

def next_question():
    global attempts

    attempts = 0

    answer_entry.delete(0, tk.END)
    answer_entry.config(fg="#05342F")
    answer_entry.focus()
    make_question()

# checking an answer

def check():
    global score, count, attempts

    try:
        guess = int(answer_entry.get())
    except ValueError:
        answer_entry.delete(0, tk.END)
        answer_entry.insert(0, "not a numberrrrrr!!")
        answer_entry.config(fg="#475F5B")

        def clear_warning():
            if answer_entry.get() == "not a numberrrrrr!!":
                answer_entry.delete(0, tk.END)
                answer_entry.config(fg="#05342F")

        answer_entry.after(1200, clear_warning)
        return

    if guess == answer:
        score += 10 if attempts == 0 else 5
        count += 1
    else:
        attempts += 1

        if attempts == 1:
            messagebox.showerror("Nuh Uh!", "Wrong answer friend... Try again!")
            answer_entry.delete(0, tk.END)
            answer_entry.focus()
            return

        messagebox.showerror("Oh Glorb..", f"Out of tries... It was {answer}!")
        count += 1

    score_update.config(text=f"Score: {score}")

    if count >= questions:
        show_results()
    else:
        next_question()

# results!!!

def show_results():

    if score == 10:
        msg = "Perfect! Mathematical!!!"
    elif score >= 8:
        msg = "Dang... Almost perfect!"
    elif score >= 5:
        msg = "You can do better!"
    else:
        msg = "Oh Glorb! Gotta practice sum more..."

    final_score.config(text=f"{score} / {questions * 10}")
    congrats_message.config(text=msg)
    display_results.tkraise()

def start_game(level):
    global difficulty, score, count, attempts

    difficulty = level
    score = 0
    count = 0
    attempts = 0

    score_update.config(text="Score: 0")
    congrats_message.config(text="")
    da_game.tkraise()
    next_question()

# annoying path error fix... solution...

main_directory = os.path.dirname(os.path.abspath(__file__))

def path(filename):
    return os.path.join(main_directory, filename)

# window

root = tk.Tk()
root.title("BMO's Maths Quiz!")

root.geometry("310x410")
root.resizable(False, False)

root.configure(bg="#25AD9F")
root.iconbitmap(path("Assets/bmo.ico"))

# load images / font

bmo_screen = ImageTk.PhotoImage(Image.open(path("Assets/bmo_screen.png")))
logo = ImageTk.PhotoImage(Image.open(path("Assets/logo.png")))

decor_buttons_1 = ImageTk.PhotoImage(Image.open(path("Assets/decor_buttons_1.png")))
decor_buttons_2 = ImageTk.PhotoImage(Image.open(path("Assets/decor_buttons_2.png")))
decor_buttons_3 = ImageTk.PhotoImage(Image.open(path("Assets/decor_buttons_3.png")))

easy_button = ImageTk.PhotoImage(Image.open(path("Assets/easy_button.png")))
medium_button = ImageTk.PhotoImage(Image.open(path("Assets/medium_button.png")))
hard_button = ImageTk.PhotoImage(Image.open(path("Assets/hard_button.png")))

entry_box = ImageTk.PhotoImage(Image.open(path("Assets/entry_box.png")))
interactable_button = ImageTk.PhotoImage(Image.open(path("Assets/interactable_button.png")))
score_bar = ImageTk.PhotoImage(Image.open(path("Assets/score_bar.png")))
submit_button = ImageTk.PhotoImage(Image.open(path("Assets/submit_button.png")))

Thunderman = "Thunderman" # impooortant: font has to be pre installed in the users system 

# ( start screen )

display_start = tk.Frame(root, bg="#25AD9F")

# background

tk.Label(display_start, image=bmo_screen, bg="#25AD9F").place(x=15, y=16)

# decorations

tk.Label(display_start, image=decor_buttons_1, bg="#25AD9F").place(x=47.77, y=210.02)
tk.Label(display_start, image=decor_buttons_2, bg="#25AD9F").place(x=51.93, y=251.11)
tk.Label(display_start, image=decor_buttons_3, bg="#25AD9F").place(x=35.81, y=346.3)

# logo

tk.Label(display_start, image=logo, bg="#B9DFCA").place(x=45.69, y=64.89)

# instructions

tk.Label(display_start, text="( Click the Red Button to Start! )", font=(Thunderman, 10), justify="center", fg="#5D7F74", bg="#B9DFCA").place(x=37, y=145)

# start button

start_button = tk.Button(display_start, image=interactable_button, bg="#25AD9F", highlightthickness=0, activebackground="#25AD9F", borderwidth=0, relief="flat", command=lambda: difficulty_menu.tkraise())
start_button.place(x=185.09, y=324.45)

# ( choose a difficulty )

difficulty_menu = tk.Frame(root, bg="#25AD9F")

# background

tk.Label(difficulty_menu, image=bmo_screen, bg="#25AD9F").place(x=15, y=16)

# decorations

tk.Label(difficulty_menu, image=decor_buttons_1, bg="#25AD9F").place(x=47.77, y=210.02)

# title

tk.Label(difficulty_menu, text="Choose The\nDifficulty!", font=(Thunderman, 26), justify="center", fg="#05342F", bg="#B9DFCA").place(x=47, y=65)

# difficulty buttons

choice_easy = tk.Button(difficulty_menu, image=easy_button, bg="#25AD9F", highlightthickness=0, activebackground="#25AD9F", borderwidth=0, relief="flat", command=lambda: start_game("Easy"))
choice_easy.place(x=20, y=263)

choice_medium = tk.Button(difficulty_menu, image=medium_button, bg="#25AD9F", highlightthickness=0, activebackground="#25AD9F", borderwidth=0, relief="flat", command=lambda: start_game("Medium"))
choice_medium.place(x=108.33, y=263)

choice_hard = tk.Button(difficulty_menu, image=hard_button, bg="#25AD9F", highlightthickness=0, activebackground="#25AD9F", borderwidth=0, relief="flat", command=lambda: start_game("Hard"))
choice_hard.place(x=196.66, y=263.5)

# ( da game itself )

da_game = tk.Frame(root, bg="#25AD9F")

# background

tk.Label(da_game, image=bmo_screen, bg="#25AD9F").place(x=15, y=16)

# decorations

tk.Label(da_game, image=decor_buttons_1, bg="#25AD9F").place(x=47.77, y=210.02)

# difficulty and question number

difficulty_label = tk.Label(da_game, text="Easy Mode / Question #1", font=(Thunderman, 12), fg="#05342F", justify="center", bg="#B9DFCA")
difficulty_label.place(x=150, y=86, anchor="center")

# question

random_question = tk.Label(da_game, text="", font=(Thunderman, 18), fg="#05342F", justify="center", bg="#B9DFCA")
random_question.place(x=150, y=126, anchor="center")

# entry box

tk.Label(da_game, image=entry_box, bg="#25AD9F", bd=0).place(x=25, y=255)

answer_entry = tk.Entry(da_game, font=(Thunderman, 12), bg="#ECF4EF", bd=0, relief="flat")
answer_entry.place(x=39, y=270, width=225, height=25)

# score bar

tk.Label(da_game, image=score_bar, bg="#25AD9F").place(x=25, y=307.66)

score_update = tk.Label(da_game, text="Score: 0", font=(Thunderman, 14), fg="#05342F", bg="#44C1DF")
score_update.place(x=93, y=350, anchor="center")

# submit button

submit_answer = tk.Button(da_game, image=submit_button, bg="#25AD9F", bd=0, highlightthickness=0, activebackground="#25AD9F", borderwidth=0, relief="flat", command=check)
submit_answer.place(x=166.24, y=311)

# ( final part / results )

display_results = tk.Frame(root, bg="#25AD9F")

# background

result_screen = tk.Label(display_results, image=bmo_screen, bg="#25AD9F")
result_screen.place(x=15, y=16)

# decor

tk.Label(display_results, image=decor_buttons_1, bg="#25AD9F").place(x=47.77, y=210.02)
tk.Label(display_results, image=decor_buttons_2, bg="#25AD9F").place(x=51.93, y=251.11)
tk.Label(display_results, image=decor_buttons_3, bg="#25AD9F").place(x=35.81, y=346.3)

# congratulations

congrats_message = tk.Label(result_screen, text="Congrats Message", font=(Thunderman, 10), fg="#05342F", bg="#B9DFCA")
congrats_message.place(relx=0.5, y=45, anchor="center")

# final score

final_score = tk.Label(result_screen, text="0 / 100", font=(Thunderman, 20), fg="#05342F", bg="#B9DFCA")
final_score.place(relx=0.5, y=100, anchor="center")

# instructions

tk.Label(display_results, text="( Click the Red Button to Play Again! )", font=(Thunderman, 8), justify="center", fg="#5D7F74", bg="#B9DFCA").place(relx=0.5, y=155, anchor="center")

# replay button

replay_button = tk.Button(display_results, image=interactable_button, bg="#25AD9F", bd=0, highlightthickness=0, activebackground="#25AD9F", borderwidth=0, relief="flat", command=lambda: display_start.tkraise())
replay_button.place(x=185.09, y=324.45)

for frame in (display_start, difficulty_menu, da_game, display_results):
    frame.place(x=0, y=0, relwidth=1, relheight=1)

display_start.tkraise()
root.mainloop()