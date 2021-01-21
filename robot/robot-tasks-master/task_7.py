#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    pass

    wall_lenght = 0

    while wall_is_beneath() == False:
        move_down()

    while wall_is_beneath() == True:
        move_right()
        wall_lenght += 1

    move_down()

    for i in range(wall_lenght):
        move_left()


if __name__ == "__main__":
    run_tasks()
