import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    source_path = os.path.join(os.getcwd(), parts[1])
    destination_path = os.path.join(os.getcwd(), parts[2])

    if destination_path.endswith("/"):
        destination_path = (os.path.join(destination_path,
                                         os.path.basename(source_path)))

    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    os.replace(source_path, destination_path)
