import shutil
import os


def move_file(command: str) -> None:
    parts = command.split()
    source_file = parts[1]
    destination_file = parts[2]
    if parts[0] == "mv" and len(parts) == 3:
        if not os.path.exists(source_file):
            with open(source_file, "w"):
                pass

        destination_dir = os.path.dirname(destination_file)
        if destination_dir and not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        shutil.move(source_file, destination_file)
