import os


def move_file(command: str) -> None:
    source_file_name, new_path = command.split()[1:]
    new_path = new_path.split("/")
    new_file_name = new_path[-1]
    if len(new_path) == 1:
        new_path = ""
    if new_path:
        new_path = "/".join(new_path[:-1]) + "/"
    if new_path:
        if not os.path.exists(new_path):
            os.makedirs(new_path)
    with (
        open(source_file_name, "r") as source_file,
        open(new_path + new_file_name, "w") as new_file
    ):
        new_file.write(source_file.read())
    os.remove(source_file_name)
