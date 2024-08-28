import os.path
from os import makedirs, rename, remove


def move_file(command: str) -> None:
    if command.split()[0] == "mv" and len(command.split()) == 3:
        command_name, source_file_name, destination_name = command.split()

        if os.path.dirname(destination_name):
            with open(source_file_name) as source:
                source_text = source.read()

            destination_folders = os.path.dirname(destination_name)
            makedirs(destination_folders, exist_ok=True)

            with open(destination_name, "w") as destination:
                destination.write(source_text)

            remove(source_file_name)
        else:
            rename(source_file_name, destination_name)
