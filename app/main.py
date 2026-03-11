import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    operation, source_path, destination_path = command_parts

    if operation != "mv":
        return

    normalized_destination = destination_path.rstrip("/\\")

    if destination_path.endswith(("/", "\\")):
        normalized_destination = os.path.join(
            normalized_destination,
            os.path.basename(source_path),
        )

    destination_directory = os.path.dirname(normalized_destination)

    if destination_directory:
        create_directories(destination_directory)

    with open(source_path, "r") as source_file:
        content = source_file.read()

    with open(normalized_destination, "w") as destination_file:
        destination_file.write(content)

    os.remove(source_path)


def create_directories(directory_path: str) -> None:
    current_path = ""

    for directory_name in directory_path.split(os.sep):
        current_path = os.path.join(current_path, directory_name)

        if not os.path.exists(current_path):
            os.mkdir(current_path)
