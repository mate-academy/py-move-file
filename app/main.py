import os.path
import shutil


def move_file(command: str) -> None:

    parts = command.split()
    mv, src, dst = parts

    if (len(parts) != 3
            or mv != "mv"
            or src == dst):
        return

    if os.path.dirname(src) == os.path.dirname(dst):
        try:
            os.rename(src, dst)
        except FileNotFoundError:
            print("File not found")
    else:
        if not os.path.exists(src):
            print("Source file does not exist.")
        elif os.path.exists(dst):
            print("Destination file already exists.")
        else:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.move(src, dst)
