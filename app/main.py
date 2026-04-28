import os


def move_file(command: str) -> None:
    context = command.split(" ")
    if len(context) != 3 or context[0] != "mv":
        return None
    if context[2].endswith("/"):
        destination = context[2] + context[1].split("/")[-1]
    else:
        destination = context[2]
    dir_path = os.path.dirname(destination)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    os.rename(context[1], destination)
