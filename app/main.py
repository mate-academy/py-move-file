import os


def move_file(command: str) -> None:
    splitted = command.split()

    if splitted[0] == "mv" and len(splitted) == 3:
        copy_command, name, path = splitted

        if "/" in path:
            dirs_names = os.path.split(path)[:-1]
            dirs_path = os.path.join(*dirs_names)
            os.makedirs(dirs_path, exist_ok=True)

        if path.endswith("/"):
            path = os.path.join(path, name)

        with open(name, "r") as file_in, open(path, "w") as file_out:
            file_out.write(file_in.read())
            os.remove(name)
