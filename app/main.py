import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    mv, source_path, destination_path = parts

    if not os.path.exists(source_path):
        return

    if os.path.isdir(destination_path):
        os.makedirs(destination_path, exist_ok=True)

    if os.path.isdir(destination_path):
        destination_file = os.path.join(destination_path,
                                        os.path.basename(source_path))
    else:
        destination_file = destination_path

    shutil.move(source_path, destination_file)
