import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) == 3 and command[0] == "mv":
        command, old_file, new_file = command
        with open(old_file, "r") as file_from:
            content = file_from.read()
        os.remove(old_file)
        path_to_new_file = os.path.dirname(new_file)
        if path_to_new_file != "":
            os.makedirs(path_to_new_file, exist_ok=True)
        with open(new_file, "w") as n_file:
            n_file.write(content)
