import os


def move_file(command: str) -> None:
    command, file_name, path = command.split()

    if command != "mv" or os.path.exists(path):
        return

    if "/" not in path:
        os.rename(file_name, path)
        return

    destination_path = os.path.split(path)[0]

    os.makedirs(destination_path, exist_ok=True)

    with (
        open(file_name, "r") as old_file,
        open(path, "w") as new_file
    ):
        new_file.write(old_file.read())

    os.remove(file_name)
