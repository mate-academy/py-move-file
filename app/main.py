import os
import shutil


def move_file(command: str) -> None:
    try:
        cmd, source, destination = command.split()
        if cmd != "mv":
            raise ValueError("Invalid command!")
        if not os.path.exists(source):
            raise FileNotFoundError(f"{source} doesn't exists!")

        dest_dir = os.path.dirname(destination)

        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)
        shutil.move(source, destination)

    except (ValueError, FileNotFoundError, PermissionError) as error:
        print(f"There was an error: {error}")
    except Exception:
        print("There was an unexpected error")
