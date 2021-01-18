# import turtle
from turtle import Screen, Turtle

screen = Screen()

turtle = Turtle()
turtle.speed(5)

# pylint detects errors in turtle code
# https://stackoverflow.com/questions/52902627/e1101module-turtle-has-no-forward-member

turtle.shape("turtle")

num_sides = 100
angle = 180 - ((num_sides - 2) * 180) / num_sides
print(angle)

# draw side
for side in range(num_sides):
    turtle.forward(5)
    turtle.left(angle)

# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)

screen.mainloop()
