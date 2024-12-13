import os


def move_file(command: str) -> None:
    command_, current_file, full_path = command.split()
    path, new_file = os.path.split(full_path)

    if command_ == "mv":
        if path:
            os.makedirs(path, exist_ok=True)

        os.replace(current_file, full_path)
