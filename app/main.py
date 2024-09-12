import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) != 3 or split_command[0] != "mv":
        print("The format is incorrect")
        return
    _, source, destination = split_command
    current_path, file_name = os.path.split(destination)
    if current_path:
        os.makedirs(current_path, exist_ok=True)
    new_file_path = os.path.join(current_path, file_name)
    os.rename(source, new_file_path)
