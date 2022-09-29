import os
import stat


def move_file(command):
    com = command.split(" ")
    os.chmod(com[1], stat.S_IWUSR)
    try:
        with open(com[1], "r") as old_file:
            info = old_file.read()

    except PermissionError:
        print("Permission ok")
        if "/" in com[2]:
            dirc = com[2].split("/")
            directory = dirc[:-1]
            new_file_name = dirc[-1]
            os.makedirs("/".join(directory))
            os.chdir("/".join(directory))
            os.remove(com[1])
            with open(new_file_name, "w") as new_file:
                new_file.write(info)
