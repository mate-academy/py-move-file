import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        cmd, origin_file, path = command_list
        if cmd == "mv":
            folders, file = os.path.split(path)
            if len(folders) > 0:
                os.makedirs(folders, exist_ok=True)
                with open(origin_file, "r") as origin, open(path, "w") as copy:
                    copy.write(origin.read())
                os.remove(origin_file)
            else:
                os.rename(origin_file, path)
