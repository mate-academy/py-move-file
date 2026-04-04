import os


def move_file(command: str) -> None:
    curr_file = command.split()
    if len(curr_file) != 3 or curr_file[0] != "mv":
        return
    old_file, new_file = curr_file[1], curr_file[2]
    path = os.path.dirname(new_file)
    if path:
        os.makedirs(path, exist_ok=True)
    with open(old_file) as old, open(new_file, "w") as new:
        new.write(old.read())
    os.remove(old_file)
