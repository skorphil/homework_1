#!/usr/bin/python3

from pyrob.api import *


def find_exit():
    right = wall_is_on_the_right()
    bottom = wall_is_beneath()
    above = wall_is_above()
    left = wall_is_on_the_left()

    if right == False:
        move_right()

    elif bottom == False:
        move_down()

    elif above == False:
        move_up()

    elif left == False:
        move_left()


@task
def task_3_3():
    pass

    find_exit()


if __name__ == "__main__":
    run_tasks()
