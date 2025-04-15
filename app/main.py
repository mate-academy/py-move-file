import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    if len(command_list) == 3 and command_list[0] == "mv":
        move, cur_file, new_file_path = command_list

        directory = os.path.dirname(new_file_path)

        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(cur_file, "r") as file_read, \
                open(new_file_path, "w") as file_write:
            file_write.write(file_read.read())
            os.remove(cur_file)
