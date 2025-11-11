import os
import shutil


def move_file(command: str) -> None:
    result = command.strip().split()
    if len(result) != 3 or result[0] != "mv":
        raise ValueError

    _, source_path, destination_path = result

    if destination_path.endswith("/"):
        destination_path = os.path.join(
            destination_path, os.path.basename(source_path)
        )

    dst_dir = os.path.dirname(destination_path)
    if dst_dir:
        os.makedirs(dst_dir, exist_ok=True)

    shutil.copy2(source_path, destination_path)
    os.remove(source_path)
