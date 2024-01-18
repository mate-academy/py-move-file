import os


def move_file(command: str) -> None:
    linux_command, old_file, path_to_new_file = command.split()
    if linux_command == "mv":
        if current_path := os.path.dirname(path_to_new_file):
            if not os.path.exists(current_path):
                os.makedirs(current_path, exist_ok=True)

    os.replace(old_file, path_to_new_file)
