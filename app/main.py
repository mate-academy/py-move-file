import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    source_path, destination_path = command_parts[1], command_parts[2]

    if source_path == destination_path or not os.path.exists(source_path):
        return

    destination_dir, destination_name = os.path.split(destination_path)
    if not destination_name:
        destination_name = os.path.basename(source_path)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)
        final_destination = os.path.join(destination_dir, destination_name)

    else:
        final_destination = destination_name

    if source_path == final_destination:
        return

    with (
        open(source_path, "r") as source_file,
        open(final_destination, "w") as destination_file,
    ):
        destination_file.write(source_file.read())

    os.remove(source_path)
