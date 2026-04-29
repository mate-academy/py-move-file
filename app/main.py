import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    if command_parts[0] != "mv":
        return

    source_file = command_parts[1]
    destination = command_parts[2]

    if destination.endswith("/"):
        destination = os.path.join(destination, source_file)

    destination_dir = os.path.dirname(destination)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    with open(source_file, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source_file)
