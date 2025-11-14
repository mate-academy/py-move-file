import os
import shutil
import shlex


def move_file(command: str) -> None:

    parts = shlex.split(command)

    if len(parts) != 3:
        raise ValueError("Command is not correct.")

    cmd, source, destination = parts

    if cmd != "mv":
        raise ValueError("Unknown command.")

    if not os.path.isfile(source):
        print("Source file does not exist")
        return

    if destination.endswith(("/", "\\")):
        destination = os.path.join(destination, os.path.basename(source))

    dir_to_create = os.path.dirname(destination)

    if dir_to_create:
        os.makedirs(dir_to_create, exist_ok=True)

    shutil.move(source, destination)
