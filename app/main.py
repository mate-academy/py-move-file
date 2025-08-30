import os.path


def move_file(command: str) -> None:

    command_list = []
    path = ""
    for com in command.split():
        command_list.extend(com.split("/"))

    if command_list[0] != "mv":
        return
    origin_file = command_list[1]
    moving_file = command_list[-1]

    for directory in command_list[2:-1]:
        if not directory:
            continue
        path += f"{directory}/"
        if not os.path.exists(path):
            os.mkdir(path)

    with (open(origin_file) as file_or,
          open(f"{path}{moving_file}", "w") as file_mv):
        file_mv.write(file_or.read())
    os.remove(origin_file)
