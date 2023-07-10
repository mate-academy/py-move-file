import os


def move_file(command: str) -> None:
    elements = command.split()
    if len(elements) == 3:
        mv_command, initial_file, path_and_copied_filename = elements
        if mv_command == "mv":
            path_to_copied_file = os.path.dirname(path_and_copied_filename)
            if path_to_copied_file:
                os.makedirs(path_to_copied_file, exist_ok=True)
            if os.path.exists(initial_file):
                os.replace(initial_file, path_and_copied_filename)
