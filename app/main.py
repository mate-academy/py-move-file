import os


def move_file(command: str) -> None:
    command, from_f, to_f = command.split(" ")
    directories = to_f.split("/")

    if to_f[-1] == "/":
        directories = directories[:-1]
        file_name_moved = from_f.split("/")[-1]
    else:
        directories, file_name_moved = directories[:-1], directories[-1]

    current_dir = ""
    for directory in directories:
        current_dir = os.path.join(current_dir, directory)
        if not os.path.exists(current_dir):
            os.mkdir(current_dir)

    new_file_path = os.path.join(current_dir, file_name_moved)
    with open(from_f, "r") as src_file:
        with open(new_file_path, "w") as dst_file:
            dst_file.write(src_file.read())

    os.remove(from_f)
