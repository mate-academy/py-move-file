import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise ValueError("Invalid command format")

    _, source_file, destination = command_parts

    directories = os.path.dirname(destination)
    if directories:
        os.makedirs(directories, exist_ok=True)

    destination_file = os.path.join(directories, os.path.basename(destination))
    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        data = file_in.read()
        file_out.write(data)

    if source_file != destination_file:
        os.remove(source_file)
