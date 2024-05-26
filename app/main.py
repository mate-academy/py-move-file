import os
import shutil

from app.validator import validation_command


def move_file(command: str) -> None:
    import shlex
    parts = shlex.split(command)
    validation_command(parts)

    source = parts[1]
    destination = parts[2]

    if not os.path.exists(source):
        raise FileNotFoundError(f"No such file or directory: '{source}'")

    if not os.path.dirname(destination):
        destination = os.path.join(os.getcwd(), destination)

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        os.makedirs(os.path.dirname(destination), exist_ok=True)

    shutil.move(source, destination)
