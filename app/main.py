import os


def move_file(command: str) -> None:
    command_line = command.split()
    if len(command_line) != 3 or command_line[0] != "mv":
        return
    _, source_file, destination = command_line
    if destination[-1] == "\\" or destination[-1] == "/":
        destination_path = destination
        destination_file = source_file
    else:
        destination_path, destination_file = os.path.split(destination)
    try:
        os.makedirs(destination_path, exist_ok=True)
    except FileNotFoundError:
        pass
    destination_path = os.path.join(destination_path, destination_file)
    try:
        with open(source_file, "r") as source, open(
            destination_path, "w"
        ) as destination:
            destination.write(source.read())
        os.remove(source_file)
    except FileNotFoundError:
        return
