import os


def move_file(command: str) -> None:
    if "mv " in command:
        command_ls = command.split()
        source_file_name = command_ls[1]
        destination_path = []
        if "/" in command_ls[2]:
            if command_ls[2].endswith("/"):
                destination_path = command_ls[2].split("/")[:-1]
                new_file_name = command_ls[1]
            else:
                destination_path = command_ls[2].split("/")[:-1]
                new_file_name = command_ls[2][command_ls[2].rfind("/") + 1:]
        else:
            new_file_name = command_ls[2]
        if destination_path:
            path_slash = [folder + "/" for folder in destination_path]
            path_buffer = ""
            for folder in path_slash:
                try:
                    os.mkdir(path_buffer + folder)
                except OSError:
                    pass
                finally:
                    path_buffer += folder
        destination_path.append(new_file_name)
        with open(source_file_name, "r") as source_file:
            with open(os.path.join(*destination_path), "w") as new_file:
                new_file.write(source_file.read())
        os.remove(source_file_name)
