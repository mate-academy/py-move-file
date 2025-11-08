from os import remove, rename, makedirs, path


def move_file(command: str) -> None:
    commands = command.split()
    if len(commands) == 3 and commands[0] == "mv":
        command, file_to_copy, new_file = commands[0], commands[1], commands[2]

        cleared_path = commands[2].split("/")
        directory = "/".join(cleared_path[:-1])
        if not cleared_path[-1]:
            new_file = file_to_copy
        else:
            new_file = cleared_path[-1]

        full_path = path.join(directory, new_file)

        if not directory:
            try:
                rename(file_to_copy, new_file)
                return
            except FileExistsError:
                raise FileExistsError

        makedirs(directory, exist_ok=True)

        try:
            with open(file_to_copy, "r") as to_copy, \
                 open(full_path, "w") as to_write:
                file_data = to_copy.readlines()
                to_write.write("".join(file_data))

            remove(file_to_copy)

        except FileNotFoundError:
            raise FileNotFoundError("[Errno 2] No such file or directory")
