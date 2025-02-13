import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3 and command_list[0] == "mv":
        from_file = command_list[1]
        to_file = command_list[2]
        print(to_file)
        if to_file.find("/") != -1:
            dir_list = to_file.split("/")
            folders_path = os.path.join("/".join(dir_list[:-1]))
            os.makedirs(folders_path, exist_ok=True)
            file_name = dir_list[-1]
            file_path = os.path.join(folders_path, file_name)
            with (open(from_file, "r") as file_to_read,
                  open(file_path, "w") as file_to_write):
                file_to_write.write(file_to_read.read())
            os.remove(command_list[1])
        else:
            os.rename(from_file, to_file)
