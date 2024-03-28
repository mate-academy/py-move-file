import os


def move_file(command: str) -> None:
    command, initial_file, destination = command.split()
    if "/" not in destination:
        os.rename(initial_file, destination)
        return
    with open(initial_file, "r") as file_in:
        content = file_in.read()
    os.remove(initial_file)
    path = os.path.dirname(destination)
    if os.path.exists(path) is False:
        os.makedirs(path)
    with open(destination, "w") as file_out:
        file_out.write(content)
