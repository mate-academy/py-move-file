import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) == 3:
        command_name, origin_path, new_path = command

        if command_name == "mv" and origin_path != new_path:
            path_name, file_name = os.path.split(new_path)
            if path_name:
                os.makedirs(path_name, exist_ok=True)
            os.rename(origin_path, new_path)

            if os.path.exists(origin_path):
                os.remove(origin_path)
