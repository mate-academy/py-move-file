import os


def move_file(command: str) -> None:
    try:
        cmd, source, destination = command.split()
    except ValueError:
        return

    if cmd != "mv":
        return

    try:
        with open(source, "r") as file_in:
            content = file_in.read()
    except FileNotFoundError:
        return

    is_directory = destination.endswith(("/", "\\"))
    destination = os.path.normpath(destination)

    if is_directory:
        dir_path = destination
        file_name = os.path.basename(source)
        destination_file = os.path.join(dir_path, file_name)
    else:
        dir_path = os.path.dirname(destination)
        destination_file = destination

    if dir_path:
        current_path = ""
        dir_parts = dir_path.split(os.path.sep)

        for part in dir_parts:
            current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(destination_file, "w") as file_out:
        file_out.write(content)

    os.remove(source)
