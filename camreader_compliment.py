import tkinter as tk
from tkinter import filedialog, Text, font
from tkinter import *
import math
from math import *
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import os
import string

WORDLIST_FILENAME = "text_detected.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading equation list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("Equation loaded.")
    return wordlist

def Addition(num1, num2):
    sum = num1 + num2
    return sum

def Subtraction(num1, num2):
    difference = num1 - num2
    return difference

def Division (num1, num2):
    quotient = num1 / num2
    return quotient

def Multiplication(num1, num2):
    product = num1 * num2
    return product

def Operator_Check(string):
    operator = ""

    if "+" in string:
        operator = "+"
    elif "*" in string:
        operator = "*"
    elif "/" in string:
        operator = "/"
    elif "X" in string:
        operator = "X"
    elif "%" in string:
        operator = "%"
    elif "-" in string:
        operator = "-"
    else:
        print("NO OPERATOR!!! YOU MESSED UP HAHAA!")

    return operator


output = load_words()
string_output = "".join(output)
print("Output: " + string_output)
no_space_output = ""

for char in string_output:
    if char != " ":
        no_space_output += char.upper()

print("No space output: " + no_space_output)
operator = Operator_Check(no_space_output)

if operator == "+":
    output_as_list = no_space_output.split("+")
    number_ans = Addition(int(output_as_list[0]), int(output_as_list[1]))

elif operator == "-":
    output_as_list = no_space_output.split("-")
    number_ans = Subtraction(int(output_as_list[0]), int(output_as_list[1]))

elif operator == "*":
    output_as_list = no_space_output.split("*")
    number_ans = Multiplication(int(output_as_list[0]), int(output_as_list[1]))

elif operator == "X":
    output_as_list = no_space_output.split("X")
    number_ans = Multiplication(int(output_as_list[0]), int(output_as_list[1]))

elif operator == "/":
    output_as_list = no_space_output.split("/")
    number_ans = Division(int(output_as_list[0]), int(output_as_list[1]))
    number_ans = int(number_ans)

else:
    number_ans = "Error!"



root = tk.Tk()
root.title('Cutie Calculator')
root.configure(bg="orange")

root.geometry("700x700")

my_font1=('Comic Sans MS', 60, 'bold')  
my_font2=('Comic Sans MS', 14)
my_font3 = ('Comic Sans MS', 12, 'bold')

l1 = tk.Label(root, text="Cutie Calculator", font=my_font1, bg="orange")
l1.pack()

if number_ans == "Error!":
    l2 = tk.Label(root, text="Error!",font=my_font2)
    l2.pack()

elif str(abs(number_ans)).isdigit():
    l2 = tk.Label(root, text = (str(no_space_output) + " = " + str(number_ans)),font=my_font2)
    l2.pack()

root.mainloop()
