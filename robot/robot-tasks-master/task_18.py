#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    pass

    while (
        wall_is_on_the_left() == False and wall_is_above() and wall_is_beneath() == True
    ):
        move_left()
    else:
        if wall_is_on_the_left() == wall_is_above():
            while wall_is_above() == True:
                move_right()
    while wall_is_above() == False:
        move_up()
    while wall_is_on_the_left() == False:
        move_left()


if __name__ == "__main__":
    run_tasks()
