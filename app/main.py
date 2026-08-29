import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    if parts[0] != "mv":
        return

    command_name, source_file_name, destination_path = parts

    if destination_path.endswith("/"):
        no_slash_destination_path = destination_path.rstrip("/")
        directories = no_slash_destination_path.split("/")
        current_path = ""

        for directory in directories:
            current_path = os.path.join(current_path, directory)

            if not os.path.exists(current_path):
                os.mkdir(current_path)

        destination_file_path = os.path.join(
            current_path,
            source_file_name
        )
    else:
        destination_directory = os.path.dirname(destination_path)
        directories = destination_directory.split("/")
        current_path = ""
        if destination_directory:
            for directory in directories:
                current_path = os.path.join(current_path, directory)
                if not os.path.exists(current_path):
                    os.mkdir(current_path)

        destination_file_path = os.path.join(
            current_path,
            os.path.basename(destination_path)
        )

    with (
        open(source_file_name, "r") as source_file,
        open(destination_file_path, "w") as destination_file
    ):
        destination_file.write(source_file.read())

    os.remove(source_file_name)
