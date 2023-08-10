import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    q = simpledialog.askstring(title="Question", prompt="Enter your question: ")
    # Make a variable and initialize it to a random number between 0 and 3
    rand = random.randint(0, 3)
    # If the random number is 0
    if rand == 0:
        messagebox.showinfo(message="Yeah, probably")
        # tell the user "Yes"

    # If the random number is 1
    elif rand == 1:
        messagebox.showinfo(message="Outlook not so good")
        # tell the user "No"

    # If the random number is 2
    elif rand == 2:
        messagebox.showinfo(message="Maybe??!??!?!!?")
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    else:
        messagebox.showinfo(message="BRUHHHHHH that's such a stupid question.")
        # write your own answer
