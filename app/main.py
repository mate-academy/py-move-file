import os


def move_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3:
        return

    command_info, file_name, destination = command_list

    if command_info != "mv":
        return

    if not os.path.isfile(file_name):
        return

    if destination.endswith("/"):
        destination = os.path.join(
            destination,
            os.path.basename(file_name)
        )

    if os.path.abspath(file_name) == os.path.abspath(destination):
        return

    directory = os.path.dirname(destination)

    if directory:
        os.makedirs(directory, exist_ok=True)

    try:
        with (
            open(file_name, "rb") as source_file,
            open(destination, "wb") as destination_file,
        ):
            destination_file.write(source_file.read())

        os.remove(file_name)

    except FileNotFoundError:
        pass
