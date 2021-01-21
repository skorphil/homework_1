#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
    pass

    for i in range(2):
        move_right()
        move_down()
    else:
        fill_cell()

    for i in range(2):
        move_right()
    move_down()


if __name__ == "__main__":
    run_tasks()
