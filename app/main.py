import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    _, source_path, destination_path = command_parts

    dest_parts = destination_path.split("/")

    if destination_path.endswith("/"):
        dir_parts = dest_parts[:-1]
        source_parts = source_path.split("/")
        file_name = source_parts[-1]
    else:
        dir_parts = dest_parts[:-1]
        file_name = dest_parts[-1]

    current_dir = ""

    for part in dir_parts:
        if not part:
            continue

        if not current_dir:
            current_dir = part
        else:
            current_dir = os.path.join(current_dir, part)

        if not os.path.exists(current_dir):
            os.mkdir(current_dir)

    if current_dir:
        final_dest_path = os.path.join(current_dir, file_name)
    else:
        final_dest_path = file_name

    with open(source_path, "r") as source_file, \
            open(final_dest_path, "w") as dest_file:

        dest_file.write(source_file.read())

    os.remove(source_path)
