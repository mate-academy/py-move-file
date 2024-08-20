import os


def move_file(command: str) -> None:
    if "/" in command:
        command = command.split()
        destination = command[2]
        file_name = command[1]
        destination_dir = os.path.dirname(destination)
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        os.rename(file_name, destination)
        if os.path.exists(file_name):
            os.remove(file_name)
    else:
        command = command.split()
        file_name = command[1]
        new_name = command[2]
        os.rename(file_name, new_name)
