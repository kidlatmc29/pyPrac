import turtle

# Creating the turtle Ted. 
ted = turtle.Pen()

# Adjusting Ted's drawing speed.
ted.speed('slow')

# Ted draws a square. 
ted.forward(50)
ted.left(90)

ted.forward(50)
ted.left(90)

ted.forward(50)
ted.left(90)

ted.forward(50)
ted.left(90)

ted.clear()

# Ted draws a square but with a for loop.
for sides in range (0,4):
    ted.forward(50)
    ted.left(90)



