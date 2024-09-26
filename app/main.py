import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")

    first_dir = parts[1]
    second_dir = parts[2]

    if not os.path.isfile(first_dir):
        raise FileNotFoundError(f"Source '{first_dir}' does not exist.")

    if second_dir.endswith("/"):
        raise (ValueError
               ("Destination cannot end with a '/'"))

    second = os.path.dirname(second_dir)

    if second:
        os.makedirs(second, exist_ok=True)
    shutil.move(first_dir, second_dir)
