import os


def move_file(command: str) -> None:
    mv, file_name, destination_path = command.split()
    if mv == "mv":
        dirs = os.path.dirname(destination_path)

        if dirs:
            os.makedirs(dirs, exist_ok=True)

        if os.path.exists(destination_path):
            os.remove(destination_path)

        os.replace(file_name, destination_path)
