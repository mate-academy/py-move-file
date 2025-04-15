import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    if len(command_list) == 3 and command_list[0] == "mv":
        move, current_file, destination_path = command_list

        directory = os.path.dirname(destination_path)

        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(current_file, "r") as file_read, \
                open(destination_path, "w") as file_write:
            file_write.write(file_read.read())
            os.remove(current_file)
