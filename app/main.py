import os


def move_file(command: str) -> None | str:
    if len(command.split()) != 3:
        return "Error. Wrong command"
    com, file_name, to_path = command.split()
    if com != "mv":
        return "Error. Wrong command"
    dirs = os.path.dirname(to_path)
    if dirs:
        os.makedirs(dirs, exist_ok=True)
    os.replace(file_name, to_path)
