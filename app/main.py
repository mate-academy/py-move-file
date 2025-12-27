import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Incorrect command format."
            "Expected format: 'mv <source> <destination>'"
        )

    _, source, destination = parts

    if destination.endswith("/"):
        full_path = os.path.join(destination, os.path.basename(source))
    else:
        full_path = destination

    dir_to_make = os.path.dirname(full_path)
    if dir_to_make:
        os.makedirs(dir_to_make, exist_ok=True)

    with open(source, "r") as f_src:
        data = f_src.read()

    with open(full_path, "w") as f_dst:
        f_dst.write(data)

    os.remove(source)
