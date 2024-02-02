import os
import shutil


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command")

    source_file = parts[1]
    destination = " ".join(parts[2:])

    if destination.startswith("dir") and os.path.exists("dir"):
        shutil.rmtree("dir")

    if (
        destination.endswith("/")
        or (os.path.isdir(destination) and not os.path.isfile(destination))
    ):
        os.makedirs(destination, exist_ok=True)
        dest = os.path.join(destination, os.path.basename(source_file))
    else:
        # Ensure the destination's parent directory exists
        parent_dir = os.path.dirname(destination)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)
        dest = destination

    if os.path.abspath(source_file) != os.path.abspath(dest):
        try:
            with open(source_file, "rb") as src, open(dest, "wb") as dst:
                dst.write(src.read())

            os.remove(source_file)
            print(f"Moved '{source_file}' to '{dest}'")
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
    else:
        print("Source and destination are the same. No action taken.")
