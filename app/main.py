import os
import shutil


def move_file(command: str) -> None:
    if len(command.split(" ")) != 3 or command.split(" ")[0] != "mv":
        return
    command_parts = command.split(" ")

    if os.path.exists(command_parts[1]):
        file_in_name = command_parts[1]
    else:
        raise FileNotFoundError("No such file you try to move")

    if command_parts[2].count("/") == 0:
        file_out_name = command_parts[2]
        os.rename(file_in_name, file_out_name)
    else:
        directory_path, file_out_name = os.path.split(command_parts[2])
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        shutil.move(
            file_in_name,
            os.path.join(directory_path, file_out_name)
        )
