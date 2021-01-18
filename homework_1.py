# import turtle
from turtle import Screen, Turtle

screen = Screen()

turtle = Turtle()

# pylint detects errors in turtle code
# https://stackoverflow.com/questions/52902627/e1101module-turtle-has-no-forward-member

turtle.shape("turtle")

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

screen.mainloop()
