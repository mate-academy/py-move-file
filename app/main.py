import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "mv":
        return None
    file_name = command[1]
    file_move = command[2].split("/")
    try:
        with open(file_name, "r") as file_read:
            copy_data = file_read.read()
        os.remove(file_name)
    except (FileNotFoundError, PermissionError):
        return None
    for index in range(len(file_move) - 1):
        try:
            os.mkdir("/".join(file_move[:index + 1]))
        except FileExistsError:
            continue
    with open("/".join(file_move), "w") as file_write:
        file_write.write(copy_data)
