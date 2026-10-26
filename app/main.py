import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    _, file_in, file_path = command_parts

    if file_path.endswith("/"):
        base_name = os.path.basename(file_in)
        file_path = os.path.join(file_path, base_name)

    if os.path.abspath(file_in) == os.path.abspath(file_path):
        return

    directory = os.path.dirname(file_path)

    if directory:
        current_dir = os.sep if os.path.isabs(directory) else ""

        for part in directory.split(os.sep):
            if not part:
                continue

            current_dir = os.path.join(current_dir, part)

            if not os.path.isdir(current_dir):
                os.mkdir(current_dir)

    with open(file_in, "r") as file, open(file_path, "w") as file_out:
        file_out.write(file.read())

    os.remove(file_in)
