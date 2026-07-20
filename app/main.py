import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise ValueError(
            "Command must be in the form: mv <source> <destination>"
        )

    _, source_file_name, destination_path = command_parts

    if destination_path.endswith("/"):
        target_path = os.path.join(
            destination_path.rstrip("/"),
            os.path.basename(source_file_name),
        )
    else:
        target_path = destination_path

    destination_directory = os.path.dirname(target_path)
    if destination_directory:
        os.makedirs(destination_directory, exist_ok=True)

    with open(source_file_name, "r") as source_file:
        content = source_file.read()

    with open(target_path, "w") as destination_file:
        destination_file.write(content)

    os.remove(source_file_name)
