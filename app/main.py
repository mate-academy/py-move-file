import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    if len(command_list) == 3:
        command_id = command_list[0]
        source_file = command_list[1]
        destination = command_list[2]
        if command_id == "mv":
            dirs = destination.split("/")
            file_name = dirs.pop()
            path = ""
            for directory in dirs:
                path += directory + "/"
                if not os.path.exists(path):
                    os.mkdir(path)
            with (
                open(source_file, "r") as source,
                open(os.path.join(path, file_name), "w") as new_file
            ):
                new_file.write(source.read())
            os.remove(source_file)
