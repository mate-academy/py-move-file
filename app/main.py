import os
import shutil


def move_file(command: str) -> None:
    split_command = command.split()
    comm, exist_file, path = split_command
    path, new_file = os.path.split(path)

    src_file = os.path.join(os.getcwd(), exist_file)

    if not path:
        os.rename(exist_file, new_file)
        return

    dst_file1 = os.path.join(os.getcwd(), path, exist_file)
    dst_file2 = os.path.join(os.getcwd(), path, new_file)

    if os.path.exists(path):
        shutil.copy(src_file, dst_file1)

        os.remove(exist_file)
        os.rename(dst_file1, dst_file2)
        return

    path = os.path.join(os.getcwd(), path)

    os.makedirs(path)

    shutil.copy(src_file, dst_file1)

    os.remove(exist_file)
    os.rename(dst_file1, dst_file2)
