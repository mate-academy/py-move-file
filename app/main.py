import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        cmd, origin_file, path = command_list[0], command_list[1], command_list[2]
        if cmd == "mv":
            folders, file = os.path.split(path)
            if len(folders) > 0:
                os.makedirs(folders, exist_ok=True)
                with open(origin_file, "r") as f, open(path, "w") as e:
                    data = f.read()
                    e.write(data)
                os.remove(origin_file)
            else:
                os.rename(origin_file, path)
