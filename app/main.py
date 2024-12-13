import os


def move_file(command: str) -> None:
    command_list = command.split()
    file_in = command_list[1]
    file_out = command_list[2]
    if file_in != file_out and command_list[0] == "mv":
        if os.path.exists(file_in):
            if "/" in file_out:
                dir_name = os.path.dirname(file_out)

                if dir_name:
                    os.makedirs(dir_name, exist_ok=True)

            with open(command_list[1], "r") as old_file, \
                    open(command_list[2], "w") as new_file:
                new_file.write(old_file.read())

            os.remove(file_in)
