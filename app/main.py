import os


def move_file(command: str) -> None:
    command_list = command.split()
    if command_list[2].find("/") != -1:
        dir_list = command_list[2].split("/")
        folders_path = "/".join(dir_list[:-1])
        os.makedirs(folders_path, exist_ok=True)
        file_name = dir_list[-1]
        file_path = os.path.join(folders_path, file_name)
        with (open(command_list[1], "r") as file_to_read,
              open(file_path, "w") as file_to_write):
            file_to_write.write(file_to_read.read())
        os.remove(command_list[1])
    else:
        os.rename(command_list[1], command_list[2])
