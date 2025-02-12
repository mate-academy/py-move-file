import shutil
from pathlib import Path


def move_file(command_file1_file2: str) -> None:
    data = command_file1_file2.split()
    if len(data) != 3 or data[0] != "mv":
        raise ValueError("Invalid command format. Use: mv source destination")

    _, src, dest = data
    src_file = Path(src)
    dest_file = Path(dest)

    try:
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(src_file, dest_file)
        print(f"File {src_file} to {dest_file} successfully")

    except FileNotFoundError:
        print("There not exist file to move")
    except ValueError as e_info:
        print(e_info)


move_file("mv file.txt first_dir/second_dir/third_dir/file.txt")
