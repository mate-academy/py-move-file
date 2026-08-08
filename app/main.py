import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    _, source_file_path, destination_path = command_parts

    if destination_path.endswith(("/", "\\")):
        destination_file_path = os.path.join(
            destination_path,
            os.path.basename(source_file_path),
        )
    else:
        destination_file_path = destination_path

    destination_directory = os.path.dirname(destination_file_path)
    if destination_directory:
        os.makedirs(destination_directory, exist_ok=True)

    with open(source_file_path, "r") as source_file:
        file_content = source_file.read()

    with open(destination_file_path, "w") as destination_file:
        destination_file.write(file_content)

    os.remove(source_file_path)
