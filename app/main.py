import os


def move_file(command: str) -> None:
    command_file = command.split()
    if len(command_file) == 3:
        command_name, source_path, destination_path = command_file

        if command_name == "mv" and source_path != destination_path:
            destination_dir, new_file_name = os.path.split(destination_path)

            if destination_dir:
                os.makedirs(destination_dir, exist_ok=True)
            os.rename(source_path, destination_path)

            if os.path.exists(source_path):
                os.remove(source_path)
