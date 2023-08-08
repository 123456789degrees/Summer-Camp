from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range (5):
        x = simpledialog.askinteger(title='Guess', prompt="Enter a guess number: ")
        # 4. Ask the user for a guess using a pop-up window, and save their response
        if x == random_num:
            messagebox.showinfo(message="You win!")
            sys.exit(0)
        elif x > random_num:
            messagebox.showinfo(message="Too high")
        else:
            messagebox.showinfo(message="Too low")
        # 5. If the guess is correct
            # 6. Win. Use 'sys.exit(0)' to end the program
    messagebox.showinfo(message="YOU LOST HAHHAHAHHAH!!!!!")

    window.mainloop()
