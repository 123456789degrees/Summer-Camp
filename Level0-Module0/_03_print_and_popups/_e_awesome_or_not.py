from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    num = random.randint(0, 3)
    # 2. Print your variable to the console
    print(num)
    # 3. Get the user to enter something that they think is awesome
    q1 = simpledialog.askstring(title='Awesome', prompt="Enter something that is awesome")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if num == 0:
        messagebox.showinfo(message="What you entered is actually awesome!")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    elif num == 1:
        messagebox.showinfo(message="What you entered is ok.")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    elif num == 2:
        messagebox.showinfo(message="What you entered is boring.")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    else:
        messagebox.showinfo(message="No wifi connection")
    # Run the window's .mainloop() method
    window.mainloop()
