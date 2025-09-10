import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    source = parts[1]
    target = parts[2]

    if not os.path.exists(source):
        return

    if os.path.isdir(target):
        destination = os.path.join(target, os.path.basename(source))
    elif target.endswith(os.sep):
        os.makedirs(target, exist_ok=True)
        destination = os.path.join(target, os.path.basename(source))
    else:
        dir_name = os.path.dirname(target)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)

        destination = target

    os.rename(source, destination)
