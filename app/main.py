import os


def move_file(command: str) -> None:
    command_name, original_file, path_to_new_file = command.split()

    if not command_name == "mv" or path_to_new_file == original_file:
        return

    path, file = os.path.split(path_to_new_file)
    if path:
        os.makedirs(os.path.join(path), exist_ok=True)

    with (open(original_file, "r") as current_file,
          open(path_to_new_file, "w") as new_file):
        new_file.write(current_file.read())

    os.remove(original_file)
