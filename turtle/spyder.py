# import turtleee
from turtle import Screen, Turtle

screen = Screen()
turtle = Turtle()

turtle.speed(5)
turtle.shape("turtle")

num_sides = 12
side_size = 40
angle = 360 / 12

for side in range(num_sides):
    turtle.forward(side_size)
    turtle.clone()
    turtle.left(180)
    turtle.forward(side_size)
    turtle.left(180 - angle)

screen.mainloop()
