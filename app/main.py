import os


def move_file(command: str) -> None:
    list_command = command.split()

    if (
        len(list_command) != 3
        or list_command[0] != "mv"
        or list_command[1] == list_command[2]
    ):
        return

    _, source, destination = list_command
    if destination.endswith("/"):
        filename = os.path.basename(source)
        destination = os.path.join(destination, filename)

    directory = os.path.dirname(destination)

    if directory:
        current_directory = ""

        for folder in directory.split("/"):
            current_directory = os.path.join(current_directory, folder)

            if not os.path.exists(current_directory):
                os.mkdir(current_directory)

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source)
