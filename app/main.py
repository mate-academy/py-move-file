import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        return
    file_name_origin = command_parts[1]
    destination = command_parts[2]

    if destination.endswith("/"):
        destination = os.path.join(
            destination,
            os.path.basename(file_name_origin)
        )

    dest_dir = os.path.dirname(destination)

    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    os.rename(file_name_origin, destination)
