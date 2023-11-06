import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) == 3 and command_parts[0] == "mv":
        _, source, destination = command_parts

        if os.path.exists(source):
            destination_dir = os.path.dirname(destination)
            if destination_dir:
                os.makedirs(destination_dir, exist_ok=True)

            os.rename(source, destination)
