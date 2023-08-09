"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from tkinter import messagebox, simpledialog, Tk
root = Tk()
num1 = simpledialog.askinteger(title="Number 1", prompt="Enter a number")
num2 = simpledialog.askinteger(title="Number 2", prompt="Enter a number")
bruh = simpledialog.askstring(title="gfdhiogudghdfigfdigsfigjishhsdruji", prompt="Add, subtract, multiply, or divide?")
if bruh.lower() == "add":
    add = num1 + num2
    messagebox.showinfo(title='', message="The sum of the numbers is " + str(add))
elif bruh.lower() == "subtract":
    sub = num1 - num2
    messagebox.showinfo(title='', message="The difference of the numbers is " + str(sub))
elif bruh.lower() == "multiply":
    mul = num1 * num2
    messagebox.showinfo(title='', message="The multiplication of the numbers is " + str(mul))
else:
    div = num1 / num2
    messagebox.showinfo(title='', message="The dividend of the numbers is " + str(div))
