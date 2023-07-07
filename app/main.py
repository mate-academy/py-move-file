import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    _, source_name, path_new_file = command_parts
    path, filename = os.path.split(path_new_file)

    if path:
        os.makedirs(path, exist_ok=True)

    with (open(source_name, "r") as source_file,
          open(path_new_file, "w") as new_file):
        new_file.write(source_file.read())

    os.remove(source_name)
