import os


def move_file(command: str) -> None:
    command_name, file, path = command.split()

    if not command_name == "mv" or file == path:
        return

    path_to_file, file_from_path = os.path.split(path)
    if len(path.split("/")) > 1:
        os.makedirs(os.path.join(path_to_file), exist_ok=True)

    with (open(file, "r") as current_file,
            open(path, "w") as new_file):
        new_file.write(current_file.read())
    os.remove(file)
