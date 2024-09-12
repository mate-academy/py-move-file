import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) != 3 or split_command[0] != "mv":
        print("The format is incorrect")
        return
    source, destination = split_command[1], split_command[2]
    parts = destination.split("/")
    file_name = parts.pop()
    current_path = ""
    for part in parts:
        current_path = os.path.join(current_path, part)
        if not os.path.exists(current_path):
            os.mkdir(current_path)
    new_file_path = os.path.join(current_path, file_name)
    os.rename(source, new_file_path)
