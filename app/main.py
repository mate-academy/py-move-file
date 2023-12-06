from os import path, makedirs, rename


def move_file(command: str) -> None:
    commands = command.split()
    if len(commands) != 3:
        raise ValueError("Invalid command format")
    cmd, source_path, destination_path = commands
    dir_path, file_name = path.split(destination_path)
    if dir_path:
        makedirs(dir_path, exist_ok=True)
    if path.exists(destination_path):
        raise FileExistsError("The file already exists.")
    rename(source_path, destination_path)
