import os
import shutil


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        print("Invalid command")
        return

    source_file = command_parts[1]
    dest = command_parts[2]

    if not os.path.exists(source_file):
        print(f"Source file {source_file} does not exist.")
        return

    dest_dirs = os.path.dirname(dest)
    if dest_dirs != "" and not os.path.exists(dest_dirs):
        os.makedirs(dest_dirs, exist_ok=True)
    shutil.move(source_file, dest)
