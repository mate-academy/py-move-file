import os


def move_file(command: str) -> None:
    command = command.split()

    if len(os.path.dirname(command[2])) > 0:
        os.makedirs(os.path.dirname(command[2]), exist_ok=True)
        with open(command[2], "w") as f:
            f.write("")
        os.remove(os.path.dirname(command[2]) + "\\" + command[1])
    else:
        os.rename(command[1], command[2])
