# write your code here
import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) >= 3:
        src_file_path = f"{parts[1]}"
        dest_file = parts[2]
    else:
        raise ValueError("You need to have 3 attributes for this to work!")

    src_content = ""
    try:
        with open(src_file_path, "r") as src_file:
            src_content = src_file.read()
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

    if "/" in dest_file:
        dest_dirs = dest_file.split("/")
        dest_file_name = dest_dirs.pop()
        dest_path = "/".join(dest_dirs)

        os.makedirs(dest_path, exist_ok=True)

    try:
        with open(f"{dest_file}", "w") as res_file:
            res_file.write(src_content)
    except Exception as e:
        print(f"An unexpected error occurred while writing the file: {e}")

    try:
        os.remove(src_file_path)
    except Exception as e:
        print(f"An unexpected error occurred while deleting the file: {e}")
