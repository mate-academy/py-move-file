import os


def move_file(command: str) -> None:

    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise ValueError("Invalid command format.")

    source_file = command_parts[1]
    destination_path = command_parts[2]

    if not os.path.exists(source_file):
        raise FileNotFoundError(f"This file {source_file} no exist.")

    if "/" not in destination_path and source_file != destination_path:
        os.rename(source_file, destination_path)
    else:
        begin_path, end_path = os.path.split(destination_path)
        os.makedirs(begin_path, exist_ok=True)
        with (
            open(source_file, "r") as file1,
            open(destination_path, "w") as file2
        ):
            file2.write(file1.read())
        os.remove(source_file)
