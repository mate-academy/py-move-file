import os


def move_file(command: str) -> None:
    command_name, old_file, new_path, *_ = command.split()

    old_path = os.path.abspath(old_file)
    new_path = os.path.abspath(new_path)

    if command_name == "mv" and old_path != new_path:
        new_dir = os.path.dirname(new_path)
        os.makedirs(new_dir, exist_ok=True)

        with open(old_path, "r") as file_out, open(new_path, "w") as file_in:
            file_in.write(file_out.read())

        os.remove(old_path)
