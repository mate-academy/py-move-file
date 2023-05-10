import os
import shutil


def move_file(command: str) -> None:
    lst = command.split(' ')
    if os.path.isfile(lst[1]):
        if lst[2].find("/") > -1 and os.path.exists(lst[2]) is False:
            new = os.path.dirname(lst[2])
            new_f = os.path.basename(lst[2])
            os.makedirs(new, exist_ok=True)
            shutil.copy2(lst[1], new + '/' + new_f)
            open(new + '/' + lst[1], "w+")
            os.remove(lst[1])

        elif os.path.isfile(lst[1]) and lst[2].find("/") < 0:
            os.rename(lst[1], lst[2])
