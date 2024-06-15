import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. "
                         "Use: mv source_file destination_file_or_directory")

    source, destination = parts[1], parts[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist")

    if destination.endswith("/"):
        if not os.path.exists(destination):
            os.makedirs(destination)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        dest_dir, _ = os.path.split(destination)
        if dest_dir and not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        if os.path.exists(destination):
            raise FileExistsError(f"Destination file '{destination}' "
                                  f"already exists")

    shutil.move(source, destination)
