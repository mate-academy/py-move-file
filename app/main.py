import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    if (command_list[0] == "mv"
            and len(command_list) == 3
            and "/" in command_list[2]):
        path_directions = command_list[2].split("/")
        make_direction = path_directions[0]
        if not os.path.exists(make_direction):
            os.mkdir(make_direction)
        if len(path_directions) > 2:
            for i in range(1, len(path_directions) - 1):
                make_direction += "/" + path_directions[i]
                if not os.path.exists(make_direction):
                    os.mkdir(make_direction)
        path = os.path.join(make_direction, path_directions[-1])
        with (open(command_list[1], "r") as file_in,
                open(path, "w") as file_out):
            for line in file_in:
                file_out.write(line)
        os.remove(command_list[1])
    elif command_list[0] == "mv" and len(command_list) == 3:
        with (open(command_list[1], "r") as file_in,
                open(command_list[2], "w") as file_out):
            for line in file_in:
                file_out.write(line)
        os.remove(command_list[1])
