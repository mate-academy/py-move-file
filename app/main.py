import os

from pathlib import Path


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3 and command_parts[0] == "mv":
        _, source_file_name, destination_file_name = command_parts
        source = Path(source_file_name)
        destination = Path(destination_file_name)
        if not source.is_file():
            return

        if destination_file_name.endswith("/"):
            destination.mkdir(parents=True, exist_ok=True)
            destination = Path(os.path.join(destination_file_name, source.name))
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)

        with open(source, "r") as source_file, open(destination, "w") as destination_file:
            destination_file.write(source_file.read())
            os.remove(source)
