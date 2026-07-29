import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")

    _, file_from, file_to = parts

    file_from_parts = file_from.split("/")

    if file_to.endswith("/"):
        file_to = os.path.join(file_to, file_from_parts[-1])

    file_to_parts = file_to.split("/")
    dirs = file_to_parts[:-1]

    current_path = ""
    for folder in dirs:
        if current_path == "":
            current_path = folder
        else:
            current_path = os.path.join(current_path, folder)

        if not os.path.exists(current_path):
            os.mkdir(current_path)

    os.rename(file_from, file_to)
