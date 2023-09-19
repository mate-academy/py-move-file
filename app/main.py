import os


def move_file(command: str) -> None:
    if "mv " in command:
        command_l = command.split()
        source_file_name = command_l[1]
        destination_path = []
        if "/" in command_l[2]:
            if command_l[2].endswith("/"):
                destination_path = command_l[2].split("/")[:-1]
                new_file_name = command_l[1]
            else:
                destination_path = command_l[2].split("/")[:-1]
                new_file_name = command_l[2][command_l[2].rfind("/") + 1:]
        else:
            new_file_name = command_l[2]
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
            print("make folder")
        destination_path.append(new_file_name)
        source_file = open(source_file_name, "r")
        buffer = source_file.read()
        source_file.close()
        os.remove(source_file_name)
        new_file = open("/".join(destination_path), "w")
        new_file.write(buffer)
        new_file.close()
