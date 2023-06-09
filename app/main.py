from os import (
    mkdir,
    remove,
    path
)


def move_file(command: str) -> None:
    command = command.split(" ")
    file_to_move = command[1]
    path_of_new_file = command[-1].split("/")
    new_file = path_of_new_file[-1]
    new_file_path = ""

    for part_of_path in path_of_new_file[:-1]:
        new_file_path = path.join(new_file_path, part_of_path)

        try:
            mkdir(new_file_path)
        except FileExistsError:
            pass

    new_file = path.join(new_file_path, new_file)

    with open(file_to_move, "r") as source, open(new_file, "w") as moved:
        for line in source:
            moved.write(line)

    remove(f"{file_to_move}")
