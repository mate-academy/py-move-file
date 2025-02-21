import os


def move_file(command: str) -> None:
    commands = command.split(" ")
    if len(commands) != 3:
        return None
    comm, original_file, target_file = commands
    if comm != "mv":
        return None
    try:
        with open(original_file, "r") as file:
            data = file.read()
    except FileNotFoundError:
        return None

    if "/" in target_file:
        *directories, target_file_name = target_file.split("/")
        path = ""
        for directory in directories:
            try:
                os.mkdir(path + directory)
            except FileExistsError:
                continue
            finally:
                path += directory + "/"
        with open(os.path.join(path + target_file_name), "w") as file:
            file.write(data)
    else:
        with open(target_file, "w") as file:
            file.write(data)
    os.remove(original_file)
