import os
import shutil


def move_file(command: str) -> None:
    linux = command.split()

    if len(linux) != 3:
        raise ValueError("Invalid command")
    if linux[0] != "mv":
        raise ValueError("Invalid command: expected 'mv'")

    source = linux[1]
    destination = linux[2]

    if not os.path.exists(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist.")
    if os.path.isdir(source):
        raise IsADirectoryError(f"Source '{source}' is a directory")

    # Перевірка, чи destination є директорією
    if destination.endswith("/"):
        if os.path.exists(destination) and not os.path.isdir(destination):
            raise FileExistsError(f"Cannot create directory '{destination}' ")
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        dir_path = os.path.dirname(destination)
        if dir_path:
            if os.path.exists(dir_path) and not os.path.isdir(dir_path):
                raise FileExistsError(f"Cannot create directory '{dir_path}' ")
            os.makedirs(dir_path, exist_ok=True)

    if os.path.exists(destination) and os.path.isdir(destination):
        destination = os.path.join(destination, os.path.basename(source))

    shutil.move(source, destination)
