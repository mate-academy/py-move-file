import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    if parts[0] != "mv":
        return

    _, file_name, dir_file_name = parts

    directory = os.path.dirname(dir_file_name)

    if dir_file_name.endswith(os.path.sep) or dir_file_name.endswith("/"):
        dir_file_name = os.path.join(dir_file_name, file_name)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(file_name, "r") as file_in:
        old_content = file_in.read()

    with open(dir_file_name, "w") as file_out:
        file_out.write(old_content)

    return os.remove(file_name)
