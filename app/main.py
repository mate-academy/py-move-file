import os
import shutil as su


def move_file(command: str) -> None:
    value = command.split(" ", 2)

    if value[0] != "mv" or len(value) != 3:
        raise ValueError(
            "Invalid command, expected 'mv <source> <destination>'"
        )

    source, target = value[1], value[2]

    if not os.path.exists(source):
        raise FileNotFoundError(f"Source file, {source}, not found")

    if target.endswith("/"):
        os.makedirs(target, exist_ok=True)
        target = os.path.join(target, os.path.basename(source))
    else:
        if os.path.dirname(target) != "":
            os.makedirs(os.path.dirname(target), exist_ok=True)

    su.move(source, target)

    print(f"Moved {source} to {target}")
