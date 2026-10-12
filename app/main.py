import os


def move_file(command: str) -> None:
    command_list = command.split(" ")

    if len(command_list) != 3 or command_list[0] != "mv":
        return

    source, destination = command_list[1], command_list[2]

    if destination.endswith(("/", os.sep)):
        destination = os.path.join(destination, os.path.basename(source))

    if source == destination or not os.path.exists(source):
        return

    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with (open(source, "r") as file_in,
          open(destination, "w") as file_out):
        for line in file_in:
            file_out.write(line)

    os.remove(source)
