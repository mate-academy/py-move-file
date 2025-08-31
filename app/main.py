import os.path


def move_file(command: str) -> None:

    command_list = command.split()
    if command_list[0] != "mv":
        return
    if len(command_list) != 3:
        return
    origin_file = command_list[1]
    path = os.path.normpath(os.path.dirname(command_list[2]))
    destination = ""

    for direct in path.split(os.path.sep):
        if direct == "":
            continue
        destination = os.path.join(destination,
                                   direct).replace(os.path.sep, "/")

        if not os.path.exists(destination):
            os.mkdir(destination)

    with (open(origin_file, "rb") as file_or,
          open(os.path.join(destination,
                            os.path.basename(command_list[2])), "wb")
          as file_mv):
        file_mv.write(file_or.read())
    os.remove(origin_file)
