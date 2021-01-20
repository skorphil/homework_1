# https://ru.wikipedia.org/wiki/%D0%90%D1%80%D1%85%D0%B8%D0%BC%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0_%D1%81%D0%BF%D0%B8%D1%80%D0%B0%D0%BB%D1%8C
from turtle import *
from math import *

color("blue")
down()
for i in range(200):
    t = i / 20 * pi
    x = (1 + 5 * t) * cos(t)
    y = (1 + 5 * t) * sin(t)
    goto(x, y)
up()
done()