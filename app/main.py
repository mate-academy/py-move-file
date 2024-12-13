import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        cmd, source_file, destination = command_list
        if cmd == "mv":
            directories = destination.split("/")
            file_name = directories.pop()
            path = ""
            for directory in directories:
                path += directory + "/"
                if not os.path.exists(path):
                    os.mkdir(path)
            with (
                open(source_file, "r") as file_in,
                open(os.path.join(path, file_name), "w") as file_out
            ):
                file_out.write(file_in.read())
            os.remove(source_file)
