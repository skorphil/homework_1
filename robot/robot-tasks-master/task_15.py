#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    pass

    if wall_is_above():
        if wall_is_on_the_left():
            for i in range(9):
                move_down()
                move_right()
        else:
            for i in range(9):
                move_down()
                move_left()
    else:
        if wall_is_on_the_left():
            for i in range(9):
                move_up()
                move_right()
        else:
            for i in range(9):
                move_up()
                move_left()


if __name__ == "__main__":
    run_tasks()
