import os


def move_file(command: str) -> None:
    action, file, direct = command.split()
    if action != "mv" or len(command.split()) != 3:
        raise ValueError
    new_direct = os.path.split(direct)[0]
    if len(new_direct):
        os.makedirs(new_direct, exist_ok=True)
    with open(file, "r") as original, open(direct, "w") as moved_file:
        moved_file.write(original.read())
    os.remove(file)
