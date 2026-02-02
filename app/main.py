import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3:
        return
    _, file_in, path = command_list
    if _ != "mv":
        return
    if path.find("/") == -1:
        os.rename(file_in, path)
        return
    if path[-1] == "/":
        os.makedirs(path, exist_ok=True)
        os.rename(f"{file_in}", os.path.join(path, file_in))
        return
    file_out = os.path.basename(path)
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    os.rename(f"{file_in}", os.path.join(directory, file_out))
