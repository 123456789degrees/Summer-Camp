
import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    s = ""
    # TODO 1) Get 6 random numbers to put on your lottery ticket
    for i in range(6):
        rand = random.randint(0, 9)
        s = s + str(rand)

    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(title="Lottery Ticket", message=s)
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
    window.mainloop()
