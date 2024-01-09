import os


def move_file(command: str) -> None:
    mv_command, file_name, file_path = command.split()
    if mv_command == "mv":
        if not os.path.dirname(file_path):
            os.replace(file_name, file_path)

        else:
            destination_path = os.path.dirname(file_path)
            if not os.path.exists(destination_path):
                os.makedirs(destination_path, exist_ok=True)
            os.replace(file_name, file_path)
