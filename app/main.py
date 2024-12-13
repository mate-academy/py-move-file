import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        return "Incorrect command!"
    mv, file_name, destination_path = command.split()
    if mv != "mv":
        return "Incorrect command!"
    dirs = os.path.dirname(destination_path)
    if dirs:
        os.makedirs(dirs, exist_ok=True)
    os.replace(file_name, destination_path)
