import os
import shutil


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "mv":
        raise ValueError(
            "Vanga (not tests or task) have told me I have to make this logic"
        )
    _, old_file, new_file = command
    path = os.path.dirname(new_file)
    if path:
        os.makedirs(path, exist_ok=True)
    shutil.copy(old_file, new_file)
    os.remove(old_file)
