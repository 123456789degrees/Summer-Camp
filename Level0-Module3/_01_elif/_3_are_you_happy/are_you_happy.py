from tkinter import Tk, simpledialog, messagebox
root = Tk()

if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    h = simpledialog.askstring(title='', prompt="Are you happy?")
    if h.lower() == "yes":
        messagebox.showinfo(title='', message="Keep doing whatever you are doing.")
    else:
        q = simpledialog.askstring(title='', prompt="Do you want to be happy?")
        if q.lower() == "yes":
            messagebox.showinfo(title='', message="Change Something")
        else:
            messagebox.showinfo(title='', message="Keep doing whatever you are doing.")
    pass
