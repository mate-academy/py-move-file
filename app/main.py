import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    if (command_list[0] == "mv"
            and len(command_list) == 3
            and "/" in command_list[2]):
        path_directions = command_list[2].split("/")
        path = path_directions[0]
        for i in range(1, len(path_directions)):
            if not os.path.exists(path):
                os.mkdir(path)
            path = os.path.join(path, path_directions[i])
    elif command_list[0] == "mv" and len(command_list) == 3:
        path = command_list[2]
    with (open(command_list[1], "r") as file_in,
            open(path, "w") as file_out):
        for line in file_in:
            file_out.write(line)
    os.remove(command_list[1])
