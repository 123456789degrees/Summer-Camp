import sys
import tkinter as tk
from tkinter import simpledialog, Tk
from PIL import Image, ImageTk
from playsound import playsound

window = None


def animals():
    global window
    window = Tk()
    window.withdraw()

    # TODO 1. Ask the user which animal they want, then see and
    #  hear the animal they chose using one of the methods below.
    while True:
        animal = simpledialog.askstring(title="Animal", prompt="Which animal do you want?")
        if animal.lower() == "cow":
            moo()
            show_image("cow.jpg")
        elif animal.lower() == "duck":
            quack()
            show_image("duck.jpg")
        elif animal.lower() == "dog":
            woof()
        elif animal.lower() == "cat":
            meow()
        elif animal.lower() == "llama":
            llama_scream()
            show_image("llama.jpg")
        else:
            sys.exit()
    # TODO 2. Make it so that the user can keep entering new animals.

    # TODO 3. If the user enters 'exit', stop the program


# ======================= DO NOT EDIT THE CODE BELOW =========================

def show_image(filename=None):
    try:
        image = Image.open(filename)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)
        return

    # Put the image on the Tk window used by simpledialog so that when the
    # window with the image is closed, the interpreter moves to the next
    # line of code
    global window
    window.deiconify()
    image = ImageTk.PhotoImage(image)
    tk.Label(master=window, image=image).pack()

    # Blocks so picture can be shown--resumes when picture window is closed
    window.mainloop()

    # Regenerate a new window after closing so more simpledialogs and
    # images can be shown
    window = Tk()
    window.withdraw()


def moo():
    playsound('moo.wav')


def quack():
    playsound('quack.wav')


def woof():
    playsound('woof.wav')


def meow():
    playsound('meow.wav')


def llama_scream():
    playsound('llama.wav')


if __name__ == '__main__':
    animals()
