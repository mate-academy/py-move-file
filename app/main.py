import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command, old_file, new_file = command.split()
        with open(old_file, "r") as file_from:
            content = file_from.read()
        os.remove(old_file)
        path_to_new_file, name_of_new_file = os.path.split(new_file)
        if path_to_new_file != "":
            os.makedirs(path_to_new_file, exist_ok=True)
            join_path = os.path.normcase(os.path.join(path_to_new_file,
                                                      name_of_new_file))
            # join_path = path_to_new_file + "/" + name_of_new_file
            with open(join_path, "w") as n_file:
                n_file.write(content)
        else:
            with open(new_file, "w") as n_file:
                n_file.write(content)
