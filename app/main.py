import os


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3 or command_split[0] != "mv":
        return None
    existing_file = command_split[1]
    new_file = command_split[2]
    try:
        os.makedirs(os.path.dirname(new_file), exist_ok=True)
    except Exception:
        pass
    try:
        with open(existing_file, "r") as e, open(new_file, "w") as n:
            n.write(e.read())
        os.remove(existing_file)
    except Exception:
        return None
