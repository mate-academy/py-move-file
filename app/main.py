import os
import shutil


def move_file(command: str) -> None:

    command_split = command.split()
    if (command_split[0] != "mv"
            or command_split[1][-4:] != command_split[2][-4:]
            or command_split[1][-4:] != ".txt"):
        raise ValueError("Error in entered data!")

    *directory, new_file = command_split[-1].split("/")

    if not directory:
        os.rename(command_split[1], new_file)
    else:
        path = ""
        for folder in directory:
            path += folder + "/"
            if not os.path.exists(path):
                os.mkdir(path)

        shutil.copy(command_split[1], command_split[-1])

        os.remove(command_split[1])
