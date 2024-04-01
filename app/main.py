import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) == 3 and command[0] == "mv":
        _, file_name, new_dir = command
        dir_path = os.path.dirname(new_dir)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        if os.path.exists(new_dir):
            os.remove(new_dir)
        os.rename(file_name, new_dir)
