import os.path


def move_file(command: str) -> None:

    command_list = command.split()
    if command_list[0] != "mv":
        return
    if len(command_list) != 3:
        return
    origin_file = command_list[1]
    destination = ""

    for direct in os.path.dirname(command_list[2]).split("/"):
        if direct == "":
            continue
        destination += os.path.join(f"{direct}/")
        if not os.path.exists(destination):
            os.mkdir(destination)

    with (open(origin_file) as file_or,
          open(os.path.join(destination,
                            os.path.basename(command_list[2])), "w")
          as file_mv):
        file_mv.write(file_or.read())
    os.remove(origin_file)
