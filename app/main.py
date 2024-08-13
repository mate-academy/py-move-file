import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3 or command_list[0] != "mv":
        raise Exception("Invalid command's format")

    _, source_file, destination = command_list

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source_file))

    destination_dir = os.path.dirname(destination)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    if os.path.dirname(destination) == os.path.dirname(source_file):
        os.rename(source_file, destination)
    else:
        try:
            with (open(source_file, "r") as source,
                  open(destination, "w") as dest):
                dest.write(source.read())
            os.remove(source_file)
        except OSError as ex:
            print(f"Error while moving file: {ex}")
