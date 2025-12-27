import os
import shutil


def move_file(command: str) -> None:

    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. "
                         "Use: mv source_path destination_path")

    source_path = parts[1]
    destination_path = parts[2]

    if not os.path.isfile(source_path):
        raise FileNotFoundError(f"Source file "
                                f"'{source_path}' does not exist")

    if destination_path.endswith("/"):
        os.makedirs(destination_path, exist_ok=True)
        destination_file = os.path.join(destination_path,
                                        os.path.basename(source_path))
    else:
        dir_path = os.path.dirname(destination_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        destination_file = destination_path

    shutil.copy2(source_path, destination_file)

    os.remove(source_path)

    print(f"File moved: '{source_path}' -> '{destination_file}'")
