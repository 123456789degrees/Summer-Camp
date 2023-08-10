import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    t = turtle.Turtle()
    t.circle(50)
    t.pensize(10)
    color = simpledialog.askstring(title="Color", prompt="Which pen color do you want?")
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    for i in range (10):
        if color.lower() == "red":
            t.pencolor(255, 0, 0)
        elif color.lower() == "green":
            t.pencolor(0, 255, 0)
        elif color.lower() == "blue":
            t.pencolor(0, 0, 255)
        else:
            t.pencolor(32, 255, 21)

    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
