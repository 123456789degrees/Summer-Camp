# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

import math
from tkinter import messagebox, simpledialog, Tk
root = Tk()
r = simpledialog.askinteger(title='Radius', prompt="Enter a radius: ")
matthewpeed = simpledialog.askstring(title='Radius', prompt="Area or circumference ")
if matthewpeed.lower() == "area":
    messagebox.showinfo(title="Area", message=r * r * math.pi)
else:
    messagebox.showinfo(title="Circumference", message=2 * r * math.pi)

#Area = πr^2
#Circumference = 2πr 
