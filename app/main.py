import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("no 'cp' command present or command syntax error")
    command, source_path, destination_path = command.split()
    if "/" not in destination_path:
        os.rename(source_path, destination_path)
    elif command == "mv" and source_path != destination_path:
        os.makedirs(os.path.dirname(destination_path))
        with (
            open(source_path, "r") as source_f,
            open(destination_path, "w") as target_f
        ):
            target_f.write(source_f.read())
            os.remove(source_path)
