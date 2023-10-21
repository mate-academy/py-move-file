from os import path, makedirs, remove


def move_file(command: str) -> None:
    mv_command, initial_file, new_file_dir = command.split()
    if mv_command == "mv":
        path_file = path.dirname(new_file_dir)
        if path_file:
            makedirs(path_file, exist_ok=True)
        with (open(initial_file, "r") as old_file,
             open(new_file_dir, "w") as new_file):
            new_file.write(old_file.read())
        remove(initial_file)
