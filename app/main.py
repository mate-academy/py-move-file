import os


def move_file(command: str) -> None:
    cc = command.split()
    if len(cc) != 3:
        return
    com, first, second = cc
    if second.endswith("/"):
        second += os.path.basename(first)
    directory = os.path.dirname(second)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(first, "rb") as source:
        content = source.read()

    with open(second, "wb") as destination:
        destination.write(content)
    os.remove(first)
