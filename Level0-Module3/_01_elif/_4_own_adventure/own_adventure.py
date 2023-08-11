from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
root = Tk()
s = simpledialog.askstring(title="", prompt="You go out to buy some groceries, and you decide to take the shortcut going through a dark alley. Unfortunately, he spots some gang members blocking the path. They are closing in on you. Do I fight them or try to negotiate peacefully?")
if s.lower() == "fight":
    q = simpledialog.askstring(title='', prompt="I quickly grab a pistol and lead pipe on the ground, and shoots one of them with the pistol. He goes down. The next one runs towards me with a katana. Should I fight or run?")
    if q == "fight":
        messagebox.showinfo(title='', message="I hit him with the lead pipe and he goes down too. YOU WIN!")
    else:
        messagebox.showinfo(title='', message="He is faster than me, and he swings. YOU LOSE")
else:
    messagebox.showinfo("A gang member shoots you and you die. YOU LOSE")
