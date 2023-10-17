import os


def move_file(command: str) -> None:
    command, first_file, second_file = command.split()
    if "/" in second_file:
        way = os.path.dirname(second_file)
        try:
            os.makedirs(way)
        except FileExistsError:
            pass
        with (open(first_file, "r") as old_file,
             open(second_file, "w") as new_file):
            content = old_file.read()
            new_file.write(content)
        os.remove(first_file)
    else:
        os.rename(first_file, second_file)
