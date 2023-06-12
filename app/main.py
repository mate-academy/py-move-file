import os


def move_file(command: str) -> None:
    command_list = command.split()
    mv, incoming_file, new_file = command_list
    dir_path, file_name = os.path.split(new_file)
    if len(command_list) != 3:
        raise IndexError("command is wrong")

    if mv == "mv":
        directory = os.path.join(dir_path)
        if dir_path:
            os.makedirs(directory, exist_ok=True)
        with (
            open(incoming_file, "r") as source_file,
            open(new_file, "w") as destination_file
        ):

            destination_file.write(source_file.read())
        os.remove(incoming_file)
