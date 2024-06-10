import os


def move_file(command: str) -> None:
    if len(command.split()) == 3 and "mv" in command.split():
        cmd, file_name, direct = command.split()
        directory = os.path.dirname(direct)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(file_name, "r") as file_r, open(direct, "w") as file_w:
            file_w.write(file_r.read())
        os.remove(file_name)
