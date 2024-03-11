import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise ValueError

    source_file = command_parts[1]
    destination = command_parts[2]

    directories, _ = os.path.split(destination)
    if directories:
        os.makedirs(directories, exist_ok=True)

    destination_file = os.path.join(directories, os.path.basename(destination))
    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        data = file_in.read()
        file_out.write(data)

    if source_file != destination_file:
        os.remove(source_file)
