import os


def movie_file(command: str) -> None:
    _, old_file, new_file = command.split()
    os.mkdir(os.path.dirname(new_file))
    with open(old_file, "r") as old_file, open(new_file, "w") as new_file:
        new_file.write(old_file.read())
