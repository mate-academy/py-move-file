from os import remove, path, mkdir


def move_file(command: str) -> None | str:
    command = command.split()
    if len(command) != 3 or command[0] != "mv":
        return "Invalid command"

    old_file = command[1]
    full_path = command[2].split("/")
    directory = full_path[:-1]
    new_file = full_path[-1]

    if not new_file:
        return "Invalid command"

    path_to_file = ""
    for folder in directory:
        path_to_file = path.join(path_to_file, folder)
        try:
            mkdir(path_to_file)
        except FileExistsError:
            pass

    path_to_file = path.join(path_to_file, new_file)
    with (
        open(old_file, "r") as orig_file,
        open(path_to_file, "w") as copied_file
    ):
        copied_file.write(orig_file.read())
        remove(old_file)
