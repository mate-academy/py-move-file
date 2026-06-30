import os


def move_file(command: str) -> None:
    file_parts = command.split()

    if len(file_parts) != 3:
        return

    action, source_file, destination_file = file_parts

    if action != "mv":
        return

    directory_path = os.path.dirname(destination_file)
    file_name = os.path.basename(destination_file)

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    final_destination = os.path.join(directory_path, file_name)

    with (
        open(source_file, "r") as source_file_object,
        open(final_destination, "w") as destination_file_object
    ):
        destination_file_object.write(source_file_object.read())

    os.remove(source_file)
