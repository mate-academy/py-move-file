import os


def move_file(command: str) -> None:
    command = command.split()
    first_file = command[1]
    second_file = command[2]
    if len(os.path.dirname(second_file)) > 0:
        os.makedirs(os.path.dirname(command[2]), exist_ok=True)
        with open(second_file, "w") as f:
            f.write("")
        os.remove(os.path.dirname(second_file) + "\\" + first_file)
    else:
        os.rename(first_file, second_file)
