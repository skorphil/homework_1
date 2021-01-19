from turtle import Screen, Turtle
from math import *

screen = Screen()

turtle = Turtle()
turtle.speed(10)

turtle.shape("turtle")

num_polygons = 10
radius = 30
x, y = 0, 0

# draw side
for polygon in range(num_polygons):
    turtle.home()
    turtle.goto(x, y)
    turtle.down()
    num_sides = 3 + polygon
    side_size = 2 * radius * sin(pi / num_sides)  # need import math to work with sin
    angle = 180 - ((num_sides - 2) * 180) / num_sides
    turtle.left(angle / 2)

    for side in range(num_sides):
        turtle.forward(side_size)
        turtle.left(angle)
    else:
        radius += 20
        y -= 20
        turtle.up()


screen.mainloop()