import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise ValueError("Invalid command format.")

    source_file, destination_path = command_parts[1:]

    if not os.path.exists(source_file):
        raise FileNotFoundError(f"This file {source_file} no exist.")

    begin_path, end_path = os.path.split(destination_path)
    if "/" in destination_path:
        os.makedirs(begin_path, exist_ok=True)
        with (
            open(source_file, "r") as source_file,
            open(destination_path, "w") as destination_path
        ):
            destination_path.write(source_file.read())
        os.remove(source_file.name)
    else:
        os.rename(source_file, destination_path)
