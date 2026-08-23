import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    operation, source, destination = command_parts

    if operation != "mv" or not os.path.isfile(source):
        return

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    destination_dir = os.path.dirname(destination)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    with (
        open(source, "r") as source_file,
        open(destination, "w") as destination_file
    ):
        destination_file.write(source_file.read())

    os.remove(source)
