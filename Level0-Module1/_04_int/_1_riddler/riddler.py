from tkinter import messagebox, simpledialog, Tk
"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""


root = Tk()

score = 0
r1 = simpledialog.askstring(title='Riddle 1', prompt="I have a little house in which I live all alone. It has no doors or windows, and if I want to go out I must break through the wall. What am I? ")
if r1.lower() == "a chick in an egg":
    score += 1
    messagebox.showinfo(title='', message="Correct")
else:
    messagebox.showinfo(title='', message="Incorrect")
r2 = simpledialog.askstring(title='Riddle 2', prompt="The more you take, the more you leave behind. What am I?")
if r2.lower() == "footsteps":
    score += 1
    messagebox.showinfo(title='', message="Correct")
else:
    messagebox.showinfo(title='', message="Incorrect")
messagebox.showinfo(title="Score", message="Your score was " + str(score))
