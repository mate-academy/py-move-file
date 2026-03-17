import os


def move_file(command: str) -> None:
    try:
        mv, existing_file, new_file = command.split()
    except ValueError:
        return None
    if mv != "mv":
        return None
    if new_file.endswith(("\\", "/")):
        new_file = os.path.join(new_file, os.path.basename(existing_file))
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
