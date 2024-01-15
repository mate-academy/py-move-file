import os


def move_file(command: str) -> None:
    mv, file_name, destination = command.split()

    if mv == "mv":
        dirs = os.path.dirname(destination)
        if dirs:
            os.makedirs(dirs, exist_ok=True)

        if os.path.exists(destination):
            os.remove(destination)

        os.replace(file_name, destination)
