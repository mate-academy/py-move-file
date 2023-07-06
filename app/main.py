import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "mv":
        raise Exception("Wrong command")

    file_path = os.path.dirname(command[2])

    if file_path:
        os.makedirs(file_path, exist_ok=True)
    os.replace(command[1], command[2])
