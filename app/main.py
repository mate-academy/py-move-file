from shutil import move
from os import makedirs
from os.path import dirname, exists


def move_file(command: str) -> None:
    try:
        cmd, source, destination = command.split()
        if cmd != "mv":
            raise ValueError("Unknown command")
        if not exists(source):
            raise FileNotFoundError(f"Unable to find the "
                                    f"source file at '{source}'")
        dest_dir = dirname(destination)
        if dest_dir:
            makedirs(dest_dir, exist_ok=True)
        move(source, destination)
    except (ValueError, FileNotFoundError) as er:
        print(f"Error: {er}")
    except Exception as er:
        print(f"Unexpected error: {er}")
