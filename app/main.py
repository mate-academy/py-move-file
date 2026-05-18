import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise ValueError(
            "Command must be in format: mv <source> <destination>"
        )

    _, source_path, destination_path = command_parts

    # Normalize separators so paths from task examples work cross-platform.
    normalized_destination = destination_path.replace("\\", "/")
    destination_parts = [
        part for part in normalized_destination.split("/") if part
    ]

    if destination_path.endswith(("/", "\\")):
        destination_parts.append(os.path.basename(source_path))

    final_destination = os.path.join(*destination_parts)
    destination_directory = os.path.dirname(final_destination)

    if destination_directory:
        normalized_directory = destination_directory.replace("\\", "/")
        directory_parts = [
            part for part in normalized_directory.split("/") if part
        ]
        current_path = ""

        for directory_part in directory_parts:
            current_path = os.path.join(current_path, directory_part)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(source_path, "r") as source_file:
        source_content = source_file.read()

    with open(final_destination, "w") as destination_file:
        destination_file.write(source_content)

    os.remove(source_path)
