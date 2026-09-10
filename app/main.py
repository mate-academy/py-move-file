import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    source_file_name = command_parts[1]
    destination_path = command_parts[2]

    if destination_path.endswith("/"):
        destination_path += os.path.basename(source_file_name)

    destination_directory = os.path.dirname(destination_path)

    if destination_directory:
        os.makedirs(destination_directory, exist_ok=True)

    with open(source_file_name, "r") as source_file:
        content = source_file.read()

    with open(destination_path, "w") as destination_file:
        destination_file.write(content)

    os.remove(source_file_name)
