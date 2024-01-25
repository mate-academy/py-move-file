import os


def move_file(command: str) -> None:
    cmd, file_name, file_path = command.split()

    if cmd == "mv":
        if os.path.dirname(file_path):
            destination = os.path.dirname(file_path)
            if not os.path.exists(destination):
                os.makedirs(destination, exist_ok=True)

        os.replace(file_name, file_path)
