import os


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3:
        return
    if command_split[0] != "mv":
        print("not mv")
        return
    command_path = command_split[2].split("/")
    try:
        if len(command_path) > 2:
            path_dir = "/".join(command_path[:len(command_path) - 1])
            if not os.path.exists(path_dir):
                os.makedirs(path_dir)
        if len(command_path) == 2:
            if not os.path.exists(command_path[0]):
                os.mkdir(command_path[0])
    except Exception:
        return
    try:
        with (open(
                command_split[1],
                "r",
                newline="",
                encoding="utf-8") as read_file,
              open(
                  command_split[2],
                  "w",
                  newline="",
                  encoding="utf-8") as write_file):
            for line in read_file:
                write_file.write(line)
        os.remove(command_split[1])
    except FileNotFoundError:
        return
