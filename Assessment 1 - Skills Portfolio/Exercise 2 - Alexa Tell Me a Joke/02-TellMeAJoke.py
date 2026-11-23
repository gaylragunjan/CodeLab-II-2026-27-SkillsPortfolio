import tkinter as tk
import os
import random

main_directory = os.path.dirname(os.path.abspath(__file__)) 

def path(filename):
    return os.path.join(main_directory, "Assets", filename)

# reading and storing jokes from a .txt file

jokes = []

with open(path("randomJokes.txt"), "r") as f:
    for line in f:
        if "?" in line:
            joke, punchline = line.split("?", 1)
            jokes.append((joke.strip(), punchline.strip()))

# show a new joke 

showing_joke = None

def new_joke():
    global showing_joke
    showing_joke = random.choice(jokes)
    joke_label.config(text=showing_joke[0] + "?")
    punch_label.config(text="")

# show punchline

def reveal_punchline():
    if showing_joke:
        punch_label.config(text=showing_joke[1])

# window 

root = tk.Tk()
root.title("Can Gayl Make You Laugh?")

root.geometry("700x400")
root.resizable(False, False)

root.configure(bg="#FFFFFF")

# labels

joke_label = tk.Label(root, text="Joke", font=("Arial", 20), fg="#322A26", bg="#FFFFFF", justify="center")
joke_label.pack()

punch_label = tk.Label(root, text="", font=("Arial", 20), fg="#322A26", bg="#FFFFFF", justify="center")
punch_label.pack()

# buttons

joke_btn = tk.Button(root, text="Whats Funny?", command=new_joke, font=("Arial", 20), fg="#000000", bg="#7B7B7B")
joke_btn.pack()

punch_btn = tk.Button(root, text="Hmm.. I dunno!", command=reveal_punchline, font=("Arial", 20), fg="#000000", bg="#7B7B7B")
punch_btn.pack()

root.mainloop()