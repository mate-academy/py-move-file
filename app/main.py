import os


def move_file(command: str) -> None:
    list_of_commands = command.split()
    if len(list_of_commands) != 3 or list_of_commands[0] != "mv":
        return
    _, source, destination = list_of_commands
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))
    directory = os.path.dirname(destination)
    if directory:
        current_directory = ""
        for part in directory.split(os.sep):
            current_directory = os.path.join(current_directory, part)
            if not os.path.exists(current_directory):
                os.mkdir(current_directory)
    with open(source, "r") as source_file, open(
        destination, "w"
    ) as destination_file:
        destination_file.write(source_file.read())
    os.remove(source)
