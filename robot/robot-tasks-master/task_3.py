#!/usr/bin/python3

from pyrob.api import *


def move_right_wall():
    wall = False
    while wall == False:
        move_right()
        wall = wall_is_on_the_right()


@task
def task_3_1():
    pass
    move_right_wall()


if __name__ == "__main__":
    run_tasks()
