import os
import shutil


def move_file(command: str) -> None:
    if not command:
        print("Error: empty command")
        return
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "mv":
        print("Error: invalid command format")
        return
    _, source, destination = parts
    if not os.path.isfile(source):
        print(f"Error: source file '{source}' does not exist")
        return
    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        parent_dir = os.path.dirname(destination)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)
    try:
        shutil.move(source, destination)
        print(f"Moved '{source}' to '{destination}'")
    except Exception as e:
        print(f"Error: {e}")
