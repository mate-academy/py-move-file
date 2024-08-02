import os


def move_file(command: str) -> None:
    command, file_name, move_to = command.split()

    path, new_file = os.path.split(move_to)

    if path and not os.path.exists(path):
        os.makedirs(path)

    try:
        with open(file_name, "r") as file, \
                open(os.path.join(path, new_file), "w") as moving:

            moving.writelines(file.readlines())

    except OSError as e:
        print(e)
    else:
        os.remove(file_name)
