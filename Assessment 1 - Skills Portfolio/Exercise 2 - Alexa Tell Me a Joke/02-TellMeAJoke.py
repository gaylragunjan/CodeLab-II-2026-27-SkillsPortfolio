import tkinter as tk
import os
import random
from PIL import Image, ImageTk
import customtkinter as ctk 

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

root.geometry("755x480")
root.resizable(False, False)

root.configure(bg="#5A5A5A")
root.iconbitmap(path("cgmyl.ico")) 

Riddleprint = "Riddleprint"
bg = ImageTk.PhotoImage(Image.open(path("the_jokester.png")))

# background

tk.Label(root, image=bg, bg="#5A5A5A").place(x=20, y=23)

# labels

joke_label = tk.Label(root, text="Wanna know something funny?", wraplength=400, font=("Riddleprint", 20), bg="#FFFCFB", fg="#322A26", justify="center")
joke_label.place(x=460, y=110, anchor="center")

punch_label = tk.Label(root, text="", wraplength=400, font=("Riddleprint", 20), bg="#FFFCFB", fg="#265F87", justify="center",)
punch_label.place(x=460, y=210, anchor="center")

# buttons

button_frame = ctk.CTkFrame(root, fg_color="#5A5A5A", corner_radius=0)
button_frame.place(relx=1.0, rely=1.0, anchor="se", x=-30, y=-10)

butt_font = ctk.CTkFont(family="Riddleprint", size=19)

butt_style = dict(
    font=butt_font,
    border_color="#000000",
    border_width=5,
    corner_radius=15,
    width=200,
    height=60,
    text_color="#000000",
    fg_color="#7B7B7B",
    hover_color="#939393",
)

joke_butt = ctk.CTkButton(button_frame, text="Whats Funny?", command=new_joke, **butt_style)
joke_butt.grid(row=0, column=0, padx=5, pady=5)

punch_butt = ctk.CTkButton(button_frame, text="Hmm.. I dunno!", command=reveal_punchline, **butt_style)
punch_butt.grid(row=0, column=1, padx=5, pady=5)

quit_butt = ctk.CTkButton(button_frame, text="Alright, I think Im done.", command=root.destroy, **butt_style)
quit_butt.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5) # haha butt

root.mainloop()