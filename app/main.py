from os import mkdir, remove, getcwd, path


def move_file(command: str) -> None:
    active_path = getcwd()
    items_command = command.split(" ")
    old_file = items_command[1]
    new_file = items_command[2].split("/")[-1]
    path_new_file = items_command[2].split("/")[0:-1]

    if path_new_file:
        for item in path_new_file:
            active_path += f"\\{item}"
            if not path.isdir(active_path):
                mkdir(active_path)

    with open(old_file, "r",) as old:
        with open(f"{active_path}\\{new_file}", "w",) as new:
            new.write(old.read())

    remove(old_file)
