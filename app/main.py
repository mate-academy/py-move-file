from os import remove, path, mkdir


def move_file(command: str) -> None | str:
    command = command.split()
    if len(command) != 3:
        return "Invalid command"

    mv, old_file, full_path = command
    if mv != "mv":
        return "Invalid command"

    path_to_file = full_path.split("/")
    if full_path.endswith("/"):
        new_file = old_file
    else:
        new_file = path_to_file[-1]
        path_to_file = path_to_file[:-1]

    new_path = ""
    for folder in path_to_file:
        new_path = path.join(new_path, folder)
        try:
            mkdir(new_path)
        except FileExistsError:
            pass

    new_path = path.join(new_path, new_file)
    with (
        open(old_file, "r") as orig_file,
        open(new_path, "w") as copied_file
    ):
        copied_file.write(orig_file.read())
        remove(old_file)
