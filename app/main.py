import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3 or command_list[0] != "mv":
        return

    _, source_path, destination_path = command_list

    directory = os.path.dirname(destination_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with (open(source_path, "r") as source_file,
          open(destination_path, "w") as destination_file):
        content = source_file.read()
        destination_file.write(content)

    os.remove(source_path)
