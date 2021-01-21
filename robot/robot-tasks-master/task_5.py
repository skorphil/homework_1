#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():
    pass

    wall = wall_is_beneath()

    while wall == True:
        move_right()
        wall = wall_is_beneath()


if __name__ == "__main__":
    run_tasks()
