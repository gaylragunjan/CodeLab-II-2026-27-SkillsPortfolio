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