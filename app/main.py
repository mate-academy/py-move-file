import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3:
        command, source_path, destination_path = command_parts
        if command == "mv":
            path, destination_file = os.path.split(destination_path)
            if path:
                os.makedirs(path, exist_ok=True)
            with (
                open(source_path, "r") as source,
                open(destination_path, "w") as destination
            ):
                destination.write(source.read())
            os.remove(source_path)
        else:
            os.rename(source_path, destination_path)
