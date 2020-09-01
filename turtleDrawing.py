import turtle

# Creating the turtle Ted. 
ted = turtle.Pen()

# Adjusting Ted's drawing speed.
ted.speed('slowest')

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


# Ted draws a square but with a while loop. 
start_x = 0
start_y = 0

ted.forward(50)
ted.left(90)

# something along the lines as ted is NOT at home (0,0), keep drawing sides of the square
while (ted.xcor() !=  start_x) and (ted.ycor() != start_y) :



