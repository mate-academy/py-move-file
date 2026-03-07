import os


def move_file(command: str) -> None:
    command_parts = command.split(" ")
    if len(command_parts) != 3 or command_parts != "mv":
        return
    path_2 = command_parts[2].split("/")
    with open(command_parts[1], "r") as file_read:
        files = file_read.read()
        if len(path_2) > 1:
            path = ""
            for part in path_2[:-1]:
                path += part + "/"
                if not os.path.isdir(path):
                    os.mkdir(path)
        with open(command_parts[2], "w") as file_write:
            file_write.write(files)
    os.remove(command_parts[1])
