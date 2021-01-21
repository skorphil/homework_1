#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    pass

    wall = wall_is_beneath()
    flag = False

    while wall == False and flag == False:
        move_right()
        wall = wall_is_beneath()
    else:
        flag = True

    while wall == True and flag == True:
        move_right()
        wall = wall_is_beneath()


if __name__ == "__main__":
    run_tasks()
