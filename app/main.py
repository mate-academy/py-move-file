import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    mv, filename, destination_path = parts
    new_file_name = ""

    if mv == "mv" and os.path.exists(filename):
        if os.path.isdir(destination_path):
            directory_path = destination_path
            new_file_name = os.path.join(directory_path, filename)
        else:
            directory_path = os.path.dirname(destination_path)
            new_file_name = destination_path

        if directory_path and not os.path.exists(directory_path):
            os.makedirs(directory_path, exist_ok=True)

    os.rename(filename, new_file_name)
