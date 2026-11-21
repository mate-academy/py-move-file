import os


def move_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3:
        return

    command_info, file_name, destination = command_list

    if command_info != "mv":
        return

    if not os.path.isfile(file_name):
        return

    if destination.find("/") != -1:
        depth = 0
        for i in range(destination.count("/")):
            depth += destination[depth:].find("/")
            if not os.path.isdir(destination[:depth]):
                os.mkdir(destination[:depth])
            depth += 1
        if destination[-1] == "/":
            destination = destination + file_name
    try:
        with (open(destination, "wb") as destination_file,
              open(file_name, "rb") as source_file):
            destination_file.write(source_file.read())
        os.remove(file_name)
    except FileNotFoundError:
        pass
