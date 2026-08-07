import os


def move_file(command: str) -> None:
    """Move a file according to a command similar to the Linux mv command."""
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Command must look like: mv <source> <destination>")

    source_path, destination_path = parts[1], parts[2]
    source_absolute_path = os.path.abspath(source_path)

    if destination_path.endswith("/"):
        target_path = os.path.join(destination_path, os.path.basename(source_path))
    else:
        target_path = destination_path

    if os.path.abspath(target_path) == source_absolute_path:
        return

    destination_directory = os.path.dirname(target_path)
    if destination_directory:
        os.makedirs(destination_directory, exist_ok=True)

    with open(source_path, "rb") as source_file:
        file_content = source_file.read()

    with open(target_path, "wb") as destination_file:
        destination_file.write(file_content)

    os.remove(source_path)
