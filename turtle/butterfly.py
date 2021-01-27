from turtle import Screen, Turtle

screen = Screen()

turtle = Turtle()
turtle.speed(10)
circle_num = 6
radius = 40


def draw_pair(radius):
    """draw circles"""
    turtle.circle(radius)
    # turtle.right(90)
    turtle.circle(-radius)


# pylint detects errors in turtle code
# https://stackoverflow.com/questions/52902627/e1101module-turtle-has-no-forward-member

turtle.shape("turtle")

for pair in range(circle_num):
    draw_pair(radius)
    radius += 5


screen.mainloop()
