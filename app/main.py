import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        raise ValueError

    if parts[0] != "mv":
        raise ValueError

    _, source_file, destination = parts

    destination_file = destination

    if destination.endswith("/"):
        destination_file = destination + os.path.basename(source_file)

    destination_dir = os.path.dirname(destination_file)

    if destination_dir:
        current_path = ""
        for part in destination_dir.split("/"):
            current_path = os.path.join(current_path,
                                        part) if current_path else part

            if not os.path.exists(current_path):
                os.mkdir(current_path)

    shutil.copy2(source_file, destination_file)

    os.remove(source_file)
