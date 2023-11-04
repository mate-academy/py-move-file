import os
from shutil import move


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        print(
            "Error: The command must contain "
            "three parts separated by spaces."
        )
        return

    mv, file_name, move_path = command.split()

    if not os.path.exists(file_name):
        print(
            f"Error: File with name: "
            f"{file_name} not found."
        )
        return

    if move_path.endswith("/"):
        directory_path = move_path
        new_file_name = os.path.join(directory_path, file_name)
    else:
        directory_path = os.path.dirname(move_path)
        new_file_name = move_path

    if directory_path and not os.path.exists(directory_path):
        os.makedirs(directory_path, exist_ok=True)

    move(file_name, new_file_name)
