import os


def move_file(command: str) -> None:
    _, source_path, destination_path = command.split()

    if destination_path.endswith("/"):
        source_file_name = os.path.basename(source_path)
        destination_path = os.path.join(destination_path, source_file_name)

    destination_dir = os.path.dirname(destination_path)

    if destination_dir:
        parts = destination_dir.split("/")
        current_path = ""
        for part in parts:
            current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(source_path, "r") as source_file:
        content = source_file.read()

    with open(destination_path, "w") as destination_file:
        destination_file.write(content)

    os.remove(source_path)
