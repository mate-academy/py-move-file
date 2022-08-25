import os
import shutil


def move_file(command):
    task = command.split()

    if "/" in task[2]:
        direction = task[2].split("/")
        for folders in range(0, len(direction) - 1):
            os.mkdir(f"{folders}")
            shutil.copyfile(task[1], task[2])
            os.remove(task[1])

    else:
        old_name = task[1]
        new_name = task[2]
        os.rename(old_name, new_name)
