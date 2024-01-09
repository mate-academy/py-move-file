import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) == 3 and split_command[0] == "mv" and split_command[1] != split_command[2]:
        directories, file_name = os.path.split(split_command[2])
        if directories:
            os.makedirs(directories, exist_ok=True)

        with open(split_command[1], "r") as f, open(split_command[2], "w") as f2:
            f2.write(f.read())

        os.remove(split_command[1])
