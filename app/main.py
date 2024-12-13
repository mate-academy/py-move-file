import os
import shutil


def move_file(command: str) -> None:
    commands = command.split()
    if len(commands) != 3 or commands[0] != "mv":
        raise ValueError("Invalid command format")

    _, source_file, destination_path = commands
    try:
        destination_dir, _ = os.path.split(destination_path)
        if destination_dir:
            os.makedirs(destination_dir, exist_ok=True)
        shutil.move(source_file, destination_path)

    except OSError as e:
        print(f"Error: {e.strerror}. Path: '{e.filename}'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
