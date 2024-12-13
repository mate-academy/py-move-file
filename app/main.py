import os


def move_file(command: str) -> None:
    cmd, file_name, file_path = command.split()

    if cmd == "mv":
        if os.path.dirname(file_path):
            destination_path = os.path.dirname(file_path)
            if not os.path.exists(destination_path):
                os.makedirs(destination_path, exist_ok=True)

        os.replace(file_name, file_path)
