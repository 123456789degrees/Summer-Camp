import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    radius = simpledialog.askinteger(title="radiys", prompt="Enter a radius in pixels:")
    # Make a new turtle
    t = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    t.circle(radius)
    # Call the turtle .penup() method
    turtle.penup()
    # Move your turtle to a new x,y position using .goto()
    turtle.goto(100, 100)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area = radius * radius * math.pi
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    t.write(arg="Area = " + str(area), move=True, align='left', font=('Arial', 20,'normal'))
    # Hide your turtle
    t.hideturtle()
    # Call turtle.done()
    turtle.done()
