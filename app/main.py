import os


def move_file(command: str) -> None:
    part = command.split()
    command_mv = part[0]
    if command_mv != "mv":
        return
    if len(part) != 3:
        print("Error: The command requires exactly 3 arguments.")
        return

    file_copy_from, file_copy_to = part[1:]
    if file_copy_to == file_copy_from:
        return

    # Ensure the destination directory exists
    dest_dir = os.path.dirname(file_copy_to)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(file_copy_from, "r") as source:
        with open(file_copy_to, "w") as destination:
            destination.write(source.read())

    os.remove(file_copy_from)
