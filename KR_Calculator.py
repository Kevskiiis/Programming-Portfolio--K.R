# Project: Simple Calculator:
# Programmer: Kevin Rodriguez
# Date: November 12, 2024

from tkinter import *

#Setup
root = Tk()
app_title = root.title ("Kevin's Calculator")
root.configure (bg="#000000")
root.resizable(0,0)
#Entry Setup
entry_box = Entry(root, width=25, borderwidth=5, font=("Helvetica",30), highlightbackground="#FFFFFF", highlightthickness=3)
entry_box.grid(row=0, column=0, columnspan=4, ipady=10,)

#Calculator Functions:
def main ():
    equation = entry_box.get()
    clear_b ()
    answer = eval (equation)
    entry_box.insert (0, str(answer))

def my_calc (numeric_value):
    number = numeric_value
    entry_box.insert (END, number)

def mathmatical_expression (math_sign):  
    expression_one = entry_box.insert (END, " ")
    math_expression = entry_box.insert (END, math_sign)
    expression_two = entry_box.insert (END, " ")

def clear_b ():
    entry_box.delete (0, END)

#Button Setup
button_1 = Button (root, text="1", width=3, height=3, padx=12, pady=10, font=("Helvetica",22), highlightbackground="#3498db", highlightthickness=3, command=lambda: my_calc("1"))
button_2 = Button (root, text="2", width=3, height=3, padx=12, pady=10, font=("Helvetica",22), highlightbackground="#3498db", highlightthickness=3, command=lambda: my_calc("2"))
button_3 = Button (root, text="3", width=3, height=3, padx=12, pady=10, font=("Helvetica",22), highlightbackground="#3498db", highlightthickness=3, command=lambda: my_calc("3"))

button_4 = Button (root, text="4", width=3, height=3, padx=12, pady=10, font=("Helvetica",22), highlightbackground="#3498db", highlightthickness=3, command=lambda: my_calc("4"))
button_5 = Button (root, text="5", width=3, height=3, padx=12, pady=10, font=("Helvetica",22), highlightbackground="#3498db", highlightthickness=3, command=lambda: my_calc("5"))
button_6 = Button (root, text="6", width=3, height=3, padx=12, pady=10, font=("Helvetica",22), highlightbackground="#3498db", highlightthickness=3, command=lambda: my_calc("6"))

button_7 = Button (root, text="7", width=3, height=3, padx=12, pady=10, font=("Helvetica",22), highlightbackground="#3498db", highlightthickness=3, command=lambda: my_calc("7"))
button_8 = Button (root, text="8", width=3, height=3, padx=12, pady=10, font=("Helvetica",22), highlightbackground="#3498db", highlightthickness=3, command=lambda: my_calc ("8"))
button_9 = Button (root, text="9", width=3, height=3, padx=12, pady=10, font=("Helvetica",22), highlightbackground="#3498db", highlightthickness=3, command=lambda: my_calc ("9"))

button_0 = Button (root, text="0", width=3, height=3, padx=12, pady=10, font=("Helvetica",22), highlightbackground="#3498db", highlightthickness=3, command=lambda: my_calc ("0"))

button_add = Button (root, text="+", width=3, height=3, padx=12, pady=10, font=("Helvetica",22), highlightbackground="#3498db", highlightthickness=3, command=lambda: mathmatical_expression ("+"))
button_sub = Button (root, text="-", width=3, height=3, padx=12, pady=10, font=("Helvetica",22), highlightbackground="#3498db", highlightthickness=3, command=lambda: mathmatical_expression ("-"))
button_multi = Button (root, text="x", width=3, height=3, padx=12, pady=10, font=("Helvetica",22), highlightbackground="#3498db", highlightthickness=3, command=lambda: mathmatical_expression ("*"))
button_divi = Button (root, text="/", width=3, height=3, padx=12, pady=10, font=("Helvetica",22), highlightbackground="#3498db", highlightthickness=3, command=lambda: mathmatical_expression ("/"))

button_enter = Button (root, text="Enter", width=3, height=3, padx=12, pady=10, font=("Helvetica",22), highlightbackground="#3498db", highlightthickness=3, command=main)
button_clear = Button (root, text="Clear", width=3, height=3, padx=12, pady=10, font=("Helvetica",22), highlightbackground="#3498db", highlightthickness=3, command=clear_b)

#Button Display
button_1.grid (row = 3, column= 2, padx=5, pady=5) 
button_2.grid (row = 3, column= 1, padx=5, pady=5)
button_3.grid (row = 3, column= 0, padx=5, pady=5)

button_4.grid (row = 2, column= 0, padx=5, pady=5)
button_5.grid (row = 2, column= 1, padx=5, pady=5)
button_6.grid (row = 2, column= 2, padx=5, pady=5)

button_7.grid (row = 1, column= 0, padx=5, pady=5)
button_8.grid (row = 1, column= 1, padx=5, pady=5)
button_9.grid (row = 1, column= 2, padx=5, pady=5)

button_0.grid (row = 4, column= 1, padx=5, pady=5)
button_clear.grid (row = 4, column= 0, padx=5, pady=5)
button_enter.grid (row = 4, column = 2, padx=5, pady=5)

button_add.grid (row=1, column=3, padx=5, pady=5)
button_sub.grid (row=2, column=3, padx=5, pady=5)
button_multi.grid (row=3, column=3, padx=5, pady=5)
button_divi.grid (row=4, column=3, padx=5, pady=5)

root.mainloop ()
