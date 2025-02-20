import os


def move_file(command: str) -> None:
    c_info = list(command.split())
    file_default = c_info[1]
    file_moved = c_info[2]

    with open(file_default, "r") as file_reader:
        reader = file_reader.read()

    if "/" not in file_moved:
        os.rename(file_default, file_moved)
    else:
        os.makedirs(os.path.dirname(file_moved), exist_ok=True)

        with open(file_moved, "w") as filee:
            filee.write(reader)

        os.remove(file_default)
