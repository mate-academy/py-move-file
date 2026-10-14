import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    _, source_path, destination_path = command_parts

    if destination_path.endswith("/"):
        destination_path += os.path.basename(source_path)

    *directory_names, destination_file_name = destination_path.split("/")

    current_directory = ""
    for directory_name in directory_names:
        current_directory = os.path.join(current_directory, directory_name)
        if not os.path.exists(current_directory):
            os.mkdir(current_directory)

    destination_file_path = os.path.join(
        current_directory, destination_file_name
    )

    with (
        open(source_path, "r") as source_file,
        open(destination_file_path, "w") as destination_file,
    ):
        destination_file.write(source_file.read())

    os.remove(source_path)
