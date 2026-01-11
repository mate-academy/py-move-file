import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command")

    src = parts[1]
    dest = parts[2]
    filename = os.path.basename(src)

    if dest.endswith("/"):
        if os.path.exists(dest) and not os.path.isdir(dest):
            raise FileExistsError(f"'{dest}'"
                                  f" already exists and is not a directory")
        os.makedirs(dest, exist_ok=True)
        dest_path = os.path.join(dest, filename)
        shutil.move(src, dest_path)
    else:
        dir_path = os.path.dirname(dest)
        if dir_path:
            if os.path.exists(dir_path) and not os.path.isdir(dir_path):
                raise FileExistsError(f"'{dir_path}'"
                                      f" already exists"
                                      f" and is not a directory")
            os.makedirs(dir_path, exist_ok=True)

        shutil.move(src, dest)
