import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    if parts[0] != "mv":
        return

    command_name, source_file_name, destination_path = parts

    if destination_path.endswith(("/", "\\")):
        no_slash_destination_path = destination_path.rstrip("/\\")
        os.makedirs(no_slash_destination_path, exist_ok=True)

        destination_file_path = os.path.join(
            no_slash_destination_path,
            source_file_name
        )
    else:
        destination_directory = os.path.dirname(destination_path)

        if destination_directory:
            os.makedirs(destination_directory, exist_ok=True)

        destination_file_path = destination_path

    with (
        open(source_file_name, "r") as source_file,
        open(destination_file_path, "w") as destination_file
    ):
        destination_file.write(source_file.read())

    os.remove(source_file_name)
