from os import remove, getcwd, path, makedirs


class IncorrectData(Exception):
    """"""


def move_file(command: str) -> None:
    items_command = command.split(" ")

    if not (items_command[0] == "mv" and len(items_command) == 3):
        raise IncorrectData("Invalid mv command")

    active_path = getcwd()
    cm, path_old_file, path_new_file = items_command
    new_path, new_file = path.split(path_new_file)
    all_path_new_file = path.join(active_path, new_path)

    if path_new_file and not path.isdir(all_path_new_file):
        makedirs(all_path_new_file)

    with open(path_old_file, "r",) as old:
        with open(path_new_file, "w",) as new:
            new.write(old.read())

    remove(path_old_file)
