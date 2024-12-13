import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) == 3 and command_parts[0] == "mv":
        mv, source_file, destination_file = command_parts

        if os.path.exists(source_file):
            destination_path = os.path.dirname(destination_file)
            if destination_path:
                os.makedirs(destination_path, exist_ok=True)

            os.rename(source_file, destination_file)
