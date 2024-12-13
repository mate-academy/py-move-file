import os


def move_file(command: str) -> None:
    command = command.split()
    if command[0] != "mv" or len(command) != 3:
        raise Exception("Wrong command!")
    file_path = os.path.dirname(command[2])

    if file_path:
        os.makedirs(file_path, exist_ok=True)
    os.replace(command[1], command[2])
