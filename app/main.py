import os


def move_file(command: str) -> None:
    parts = command.split()
    file_from = parts[1]
    file_to = parts[2]

    file_from_parts = file_from.split("/")

    if file_to.endswith("/"):
        file_to = file_to + file_from_parts[-1]

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
