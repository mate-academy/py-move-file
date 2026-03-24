import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    _, source_path, destination_path = command_parts

    if destination_path.endswith(os.sep):
        create_directories(destination_path.rstrip(os.sep))
        destination_path = (
            os.path.join(destination_path,
                         os.path.basename(source_path))
        )
    else:
        destination_directory = os.path.dirname(destination_path)
        if destination_directory:
            create_directories(destination_directory)

    with open(source_path, "r") as source_file:
        file_content = source_file.read()

    with open(destination_path, "w") as destination_file:
        destination_file.write(file_content)

    os.remove(source_path)


def create_directories(path: str) -> None:
    current_path = ""

    for directory in path.split(os.sep):
        current_path = os.path.join(current_path, directory)
        if not os.path.exists(current_path):
            os.mkdir(current_path)
