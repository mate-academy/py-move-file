import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        return
    _, file_name_origin, destination = command_parts

    if destination.endswith("/"):
        destination = os.path.join(
            destination,
            os.path.basename(file_name_origin)
        )

    dest_dir = os.path.dirname(destination)

    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with (open(file_name_origin) as old_file,
          open(destination, "w") as new_file):
        content = old_file.read()
        new_file.write(content)
    os.remove(file_name_origin)
