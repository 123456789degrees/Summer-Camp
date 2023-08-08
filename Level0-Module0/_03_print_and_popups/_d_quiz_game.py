from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete

    # Make a new window variable, window = Tk()
window = Tk()
    # Hide the window using the window's .withdraw() method
window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
score = 0

    # ASK A QUESTION AND CHECK THE ANSWER
q1 = simpledialog.askstring(title='1+1?', prompt="What is 1+1?")
    #      // 2.  Ask the user a question 
if q1 == str(1):
    messagebox.showinfo(message="CORRECT")
    score += 1
    #      // 3.  Use an if statement to check if their answer is correct
else:
    messagebox.showinfo(message="INCORRECT")
    score -= 1
    #      // 4.  if the user's answer was correct, add one to their score 
q2 = simpledialog.askstring(title='BEST', prompt="Is Joshua the best person in the world?")
if q2.lower() == "yes":
    messagebox.showinfo(message="CORRECT")
    score += 1
else :
    messagebox.showinfo(message="INCORRECT")
    score -= 1
q3 = simpledialog.askstring(title='12/3', prompt="What is 12/3?")
if q3 == str(4):
    messagebox.showinfo(message="CORRECT")
    score += 1
else:
    messagebox.showinfo(message="INCORRECT")
    score -= 1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
messagebox.showinfo(message=str(score))
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
