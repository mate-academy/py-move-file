import os


def move_file(command: str) -> None:
    cmd, first_file, second_file = command.split()
    if cmd == "mv" and first_file != second_file:
        if os.path.exists(first_file):
            directory_path = os.path.dirname(second_file)
            if directory_path:
                os.makedirs(directory_path, exist_ok=True)
            with (open(first_file, "r") as old_file,
                  open(second_file, "w") as new_file):
                new_file.write(old_file.read())
            os.remove(first_file)
