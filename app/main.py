from os import remove, path, makedirs


def move_file(command: str) -> None:
    command_input, path_info, file_name = command.split()
    if len(command.split()) == 3 or command_input != "mv":
        move_to, name = path.split(file_name)
        if move_to:
            makedirs(move_to, exist_ok=True)
        with open(path_info, "r") as file_in, open(file_name, "w") as file_out:
            file_out.write(file_in.read())
        remove(path_info)
