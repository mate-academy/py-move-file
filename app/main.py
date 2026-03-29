import os


def move_file(command: str) -> None:
    if not len(command.split()) == 3:
        print("command not found")

    command, file_name, path = command.split()
    dir_path = ""

    for directory in path.split("/"):
        if "." not in directory:
            dir_path += (directory + "/")
            try:
                os.mkdir(dir_path)
            except FileExistsError:
                print("ok")
    try:
        with (
            open(file_name, "r") as file_original,
            open(path, "w") as file_clone
        ):

            file_clone.write(file_original.read())

    except FileNotFoundError:
        print("file not found")

    os.remove(file_original.name)
