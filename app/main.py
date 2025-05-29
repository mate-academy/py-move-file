import os
import shutil


def move_file(command: str) -> None:
    src_file = command.split()[1]
    destination = command.split()[2]
    cmd = command.split()[0]
    des_path = os.path.dirname(destination)

    if (cmd == "mv" and os.path.exists(src_file)):
        if "/" not in destination:
            os.rename(src_file, destination)
        else:
            os.makedirs(des_path, exist_ok=True)
            if not os.path.exists(destination):
                shutil.copy(src_file, destination)
                os.remove(src_file)
