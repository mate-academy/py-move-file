import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        return

    command_keyword, source_path, destination_path = command_parts
    if command_keyword != "mv":
        return

    if destination_path.endswith("/"):
        destination_path = os.path.join(
            destination_path, os.path.basename(source_path)
        )

    if os.path.abspath(source_path) == os.path.abspath(destination_path):
        return

    directory = os.path.dirname(destination_path)
    current_directory = ""

    for part in directory.split(os.sep):
        if not part:
            if not current_directory and directory.startswith(os.sep):
                current_directory = os.sep
            continue

        current_directory = os.path.join(current_directory, part)
        if not os.path.exists(current_directory):
            os.mkdir(current_directory)

    with open(source_path, "rb") as source:
        content = source.read()

    with open(destination_path, "wb") as destination:
        destination.write(content)

    os.remove(source_path)
