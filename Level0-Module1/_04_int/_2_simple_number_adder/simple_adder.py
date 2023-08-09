"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
import sys
from tkinter import messagebox, simpledialog, Tk
root = Tk()
num1 = simpledialog.askinteger(title="Number 1", prompt="Enter a number")
num2 = simpledialog.askinteger(title="Number 2", prompt="Enter a number")
add = num1 + num2
if add == 69 or add == 420:
    messagebox.showinfo(title="Sum", message="The sum of the two numbers is a sussyyyyyyy number")
    sys.exit()
messagebox.showinfo(title="Sum", message="The sum of the two numbers is " + str(add))
