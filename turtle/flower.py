from turtle import Screen, Turtle

screen = Screen()

turtle = Turtle()
turtle.speed(10)
leaf_num = 6
radius = 40
pair_num = int(leaf_num / 2)


def draw_pair(radius):
    turtle.circle(radius)
    # turtle.right(90)
    turtle.circle(-radius)


# pylint detects errors in turtle code
# https://stackoverflow.com/questions/52902627/e1101module-turtle-has-no-forward-member

turtle.shape("turtle")

for pair in range(pair_num):
    angle = 360 / leaf_num
    draw_pair(radius)
    turtle.right(angle)


screen.mainloop()