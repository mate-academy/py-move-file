import os


def move_file(command: str) -> None:
    mode, old_filename, fullpath_to_file = command.split()
    path_to_file = os.path.split(fullpath_to_file)[0]

    if mode == "mv" and old_filename != fullpath_to_file:
        if path_to_file != "" and not os.path.exists(path_to_file):
            os.makedirs(path_to_file)

        with open(
                old_filename, "r"
        ) as old_file, open(
            fullpath_to_file, "w"
        ) as new_file:

            new_file.write(old_file.read())
        os.remove(old_filename)
