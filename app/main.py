import os
import shutil


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise SystemError("Command 'mv' must accept 3 arguments")

    _, source_path, destination_path = command.split()
    if destination_path.count("/") == 0:
        os.rename(source_path, destination_path)

    else:
        if not os.path.exists(os.path.dirname(destination_path)):
            if destination_path.count(".") == 0:
                os.makedirs(destination_path)
            else:
                os.makedirs(os.path.dirname(destination_path))

        shutil.copy(source_path, destination_path)
        os.remove(source_path)
