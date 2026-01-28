import os


def move_file(command: str) -> None:
    _command = command.split()
    if len(_command) == 3:
        mv, file_name, path = _command

    if mv == "mv" and "/" not in path:
        os.rename(file_name, path)
    elif mv == "mv" and "/" in path:
        split_path = path.split("/")
        path_without_file_name = "/".join(split_path[:-1])
        new_file_name = split_path[-1]

        os.makedirs(path_without_file_name, exist_ok=True)

        with (open(f"{path_without_file_name}/{new_file_name}", "w") as new,
              open(file_name, "r") as old):
            new.write(old.read())
            os.remove(file_name)
