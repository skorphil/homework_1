# import turtleee
from turtle import Screen, Turtle

screen = Screen()

turtle = Turtle()
turtle.speed(10)

turtle.shape("turtle")

num_polygons = 10
init_offset = 10
num_sides = 4
side_size = 10
angle = 180 - ((num_sides - 2) * 180) / num_sides
print(angle)

x = 0
y = 0


# draw side
for polygon in range(num_polygons):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for side in range(num_sides):
        turtle.forward(side_size)
        turtle.left(angle)
    else:
        x = x - init_offset
        y = y - init_offset
        side_size = side_size + 2 * init_offset


screen.mainloop()
