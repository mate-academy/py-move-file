import os


def move_file(path: str) -> None:
    parts = path.split(" ")
    root_file = parts[1]
    new_path = parts[-1]

    new_path_only_directory = new_path.split("/")[:-1]
    current_path = ""
    for directory in new_path_only_directory:
        current_path = os.path.join(current_path, directory)
        print(current_path)
        if not os.path.isdir(current_path):
            os.mkdir(current_path, mode=0o777)

    with open(root_file, "r") as source_file, open(new_path, "w") as \
            destination_file:
        destination_file.write(source_file.read())

    os.remove(root_file)
