import turtle

if __name__ == '__main__':
    t = turtle.Turtle()
    t.shape('turtle')
    t.color('blue', 'green')
    t.speed(100)
    t.penup()
    # TODO 1) Set the X position of the turtle so that it starts on the left.
    t.setx(-400)
    # TODO 2) Make the turtle draw a star shape. Hint: angle=144.\
    t.penup()
    for i in range (5):
        t.forward(30)
        t.right(144)
    # TODO 3) Set the length of each line in the star to 30

    # TODO: CHALLENGE
    #       Make the turtle draw a line of stars like the image in
    #       this folder.
    #       Hint: The distance between stars is 50.

# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
