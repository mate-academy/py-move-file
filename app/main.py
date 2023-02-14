import os


def move_file(command: str) -> None:
    if command.startswith("mv"):
        if "/" not in command:
            command, old_name, new_name = command.split()
            os.rename(old_name, new_name)

        command, file, path = command.split()
        os.makedirs(path[:path.rfind("/")])
        os.replace(file, path)
