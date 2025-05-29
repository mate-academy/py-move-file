import os
import shutil


def move_file(command: str) -> None:
    src_file = command.split()[1]
    destination = command.split()[2]
    cmd = command.split()[0]

    if (cmd == "mv" and os.path.exists(src_file)):
        if destination == os.path.basename(destination):
            os.rename(src_file, destination)
        else:
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            if not os.path.exists(destination):
                try:
                    shutil.copy(src_file, destination)
                    os.remove(src_file)
                except Exception as e:
                    print(f"Unexpected error: {e}")
