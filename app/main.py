import os

def move_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3 or command_list[0] != "mv":
        return

    _, source, destination = command_list

    if source == destination:
        return

    destination_dir = os.path.dirname(destination)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    if os.path.isdir(destination):
        raise IsADirectoryError(f"'{destination}' is a directory, not a file.")

    with open(source, "r") as src_file, open(destination, "w") as dst_file:
        dst_file.write(src_file.read())

    os.remove(source)
