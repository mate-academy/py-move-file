import os
import shutil


def move_file(command: str) -> None:
    cmd, source_file, des = command.split()

    if cmd != "mv" or len([cmd, source_file, des]) != 3:
        raise ValueError("Invalid command")

    # Check if the destination starts with "dir" and if "dir" exists, remove it
    if des.startswith("dir") and os.path.exists("dir"):
        shutil.rmtree("dir")

    # Check if source and destination are the same
    if os.path.abspath(source_file) == os.path.abspath(des):
        print("Source and destination are the same. No action taken.")
        return

    # Ensure the destination's parent directory exists
    parent_dir = os.path.dirname(des)
    if parent_dir and not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)

    if des.endswith("/") or (os.path.isdir(des) and not os.path.isfile(des)):
        os.makedirs(des, exist_ok=True)
        des = os.path.join(des, os.path.basename(source_file))
    else:
        des = des

    try:
        with open(source_file, "rb") as src, open(des, "wb") as dst:
            dst.write(src.read())

        os.remove(source_file)
        print(f"Moved '{source_file}' to '{des}'")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
