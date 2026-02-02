import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) == 3 and split_command[0] == "mv":
        cmd, file_name, direct = split_command
        directory = os.path.dirname(direct)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(file_name, "r") as file_r, open(direct, "w") as file_w:
            file_w.write(file_r.read())
        os.remove(file_name)
