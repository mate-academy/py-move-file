import os


def move_file(command: str) -> None:
    commands = command.split()

    if len(commands) == 3 and commands[0] == "mv":

        source_file_path, destination_file_path = commands[1:]

        destination_dir, file_name = os.path.split(destination_file_path)

        if destination_dir and not os.path.exists(destination_dir):
            os.makedirs(destination_dir, exist_ok=True)

        os.rename(source_file_path, destination_file_path)
