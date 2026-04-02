import os.path


def move_file(command: str) -> None:
    command_name, file_orig, file_new = command.split()
    if command_name != "mv":
        return

    if not os.path.dirname(file_new):
        os.replace(file_orig, file_new)
    else:
        path = os.path.dirname(file_new)
        os.makedirs(path, exist_ok=True)
        os.replace(file_orig, file_new)
