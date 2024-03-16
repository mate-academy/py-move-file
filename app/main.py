import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if parts[0] != "mv" or len(parts) != 3:
        raise ValueError("Command should be in the format:"
                         " 'mv source_file destination_path'")

    source, destination = parts[1], parts[2]

    if not os.path.exists(source):
        raise FileNotFoundError(f'The source file "{source}" does not exist.')

    if destination.endswith("/") or (os.path.isdir(destination)
                                     and not os.path.isfile(destination)):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        destination_dir = os.path.dirname(destination)
        if destination_dir and not os.path.exists(destination_dir):
            os.makedirs(destination_dir, exist_ok=True)
    shutil.move(source, destination)
