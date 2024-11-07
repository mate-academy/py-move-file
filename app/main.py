import os
import shutil


def move_file(command: str) -> None:
    data = command.split(" ")
    if data[0] == "mv" and len(data) == 3:
        source_file = data[1]
        destination = data[2]

        if not os.path.exists(source_file):
            raise FileNotFoundError(f"File {source_file} does not exist.")

        if destination.endswith("/"):
            if not os.path.exists(destination):
                os.makedirs(destination, exist_ok=True)
            destination = os.path.join(destination,
                                       os.path.basename(source_file))
        else:
            destination_dir = os.path.dirname(destination)
            if destination_dir:
                os.makedirs(destination_dir, exist_ok=True)

        shutil.move(source_file, destination)
