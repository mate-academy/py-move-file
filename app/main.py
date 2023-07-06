import os


def move_file(command: str) -> None:
    command_split = command.split()
    command_name, source_path, dest_path = command_split
    if len(command_split) != 3 or command_name != "mv":
        raise Exception("Wrong command")

    file_path = os.path.dirname(dest_path)

    if file_path:
        os.makedirs(file_path, exist_ok=True)
    os.replace(source_path, dest_path)
