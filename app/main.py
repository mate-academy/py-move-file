import os


def move_file(command: str) -> None:
    commands_list = command.split()
    if len(commands_list) != 3 or commands_list[0] != "mv":
        return

    source, destination = commands_list[1], commands_list[2]

    if source == destination or not os.path.isfile(source):
        return

    if destination.endswith("/") or os.path.isdir(destination):
        destination = os.path.join(destination, os.path.basename(source))

    directory = os.path.dirname(destination)

    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    try:
        with (
            open(source, "rb") as file_in,
            open(destination, "wb") as file_out
        ):
            file_out.write(file_in.read())
    except OSError:
        return
    else:
        os.remove(source)
