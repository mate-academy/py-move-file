import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source_path, destination_path = parts

    try:
        with open(source_path, "r") as file:
            content = file.read()
    except FileNotFoundError:
        return

    if "/" in destination_path:
        path_parts = destination_path.split("/")

        if destination_path.endswith("/"):
            directories = path_parts[:-1]
            file_name = os.path.basename(source_path)
            destination_path = destination_path + file_name
        else:
            directories = path_parts[:-1]

      current_path = ""

for directory in directories:
    if not directory:
        continue

    current_path = (
        directory
        if not current_path
        else os.path.join(current_path, directory)
    )

    if not os.path.exists(current_path):
        os.mkdir(current_path)
