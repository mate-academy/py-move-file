import os
import os.path


def move_file(command: str) -> None:
    try:
        command_name, main_file, path_to_file = command.split()
    except ValueError:
        return
    if command_name != "mv":
        return
    if path_to_file.endswith("/"):
        new_directory = path_to_file
        path_file = os.path.join(
            path_to_file,
            os.path.basename(main_file)
        )
    else:
        path_file = path_to_file
        new_directory = os.path.dirname(path_to_file)
    if main_file == path_file:
        return
    if new_directory:
        try:
            os.makedirs(new_directory, exist_ok=True)
        except (PermissionError, OSError):
            return

    try:
        with open(main_file, "r") as file_in, open(path_file, "w") as file_out:
            file_out.write(file_in.read())
        os.remove(main_file)
    except FileNotFoundError:
        return
