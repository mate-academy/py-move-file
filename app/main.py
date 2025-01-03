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
    with open(src_file_path, "r") as src_file:
        src_content = src_file.read()

    root_dir = os.getcwd()
    if "/" in dest_file:
        dest_dirs = dest_file.split("/")
        dest_file_name = dest_dirs.pop()

        if len(dest_dirs) > 1:
            for directory in dest_dirs:
                if not os.path.exists(directory):
                    os.mkdir(f"{directory}")
                os.chdir(f"{directory}")
        else:
            dest_file_path = dest_dirs[0]
            if not os.path.exists(dest_file_path):
                os.mkdir(dest_file_path)
            os.chdir(dest_file_path)
    else:
        dest_file_name = dest_file

    with open(f"./{dest_file_name}", "w") as dest_file:
        dest_file.write(src_content)

    os.chdir(root_dir)
    os.remove(src_file_path)
