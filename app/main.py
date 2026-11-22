from os import mkdir, remove


def move_file(command: str) -> None:
    command = command.split()
    old_file = command[1]
    path = command[2].split("/")
    directory = path[:-1]
    new_file = path[-1]

    path_to_file = ""
    for folder in directory:
        try:
            mkdir(path_to_file + folder)
        except FileExistsError:
            pass
        finally:
            path_to_file += f"{folder}/"

    with (
        open(old_file, "r") as orig_file,
        open(path_to_file + new_file, "w") as copied_file
    ):
        copied_file.write(orig_file.read())
        remove(old_file)
