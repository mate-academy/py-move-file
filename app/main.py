import os


def move_file(command: str) -> None:

    try:
        command_name, source_path, destination_path = command.split()
    except ValueError:
        return

    if command_name != "mv":
        return

    if destination_path.endswith('/'):
        file_name = os.path.basename(source_path)
        full_destination_path = os.path.join(destination_path, file_name)
    else:
        full_destination_path = destination_path

    if source_path == full_destination_path:
        return


    dest_dir = os.path.dirname(full_destination_path)
    if dest_dir:
        current_path = ""
        for part in dest_dir.split(os.sep):
            current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    try:
        with open(source_path, "r") as file_in, open(full_destination_path, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
        os.remove(source_path)
    except FileNotFoundError:
        pass
