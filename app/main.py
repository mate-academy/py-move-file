import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source_file_name, destination_path = parts

    if not os.path.isfile(source_file_name):
        raise FileNotFoundError(f"Source file '{source_file_name}' does not exist or is not a file.")

    if destination_path.endswith("/"):
        destination_path = os.path.join(destination_path, os.path.basename(source_file_name))

    destination_dir = os.path.dirname(destination_path)
    if destination_dir:
        current_path = ""
        for folder in destination_dir.split("/"):
            current_path = os.path.join(current_path, folder)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(source_file_name, "r", encoding="utf-8") as source_file, \
            open(destination_path, "w", encoding="utf-8") as destination_file:
        destination_file.write(source_file.read())

    os.remove(source_file_name)
