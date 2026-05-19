import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    source_file = parts[1]
    target = parts[2]

    if not os.path.exists(source_file):
        return

    if target.endswith("/"):
        directory = target[:-1]
        destination_file = os.path.join(target, os.path.basename(source_file))
    else:
        directory = os.path.dirname(target)
        destination_file = target

    if directory:
        try:
            os.makedirs(directory, exist_ok=True)
        except FileExistsError:
            pass

    with open(source_file, "r") as file_in, open(
        destination_file, "w"
    ) as file_out:
        file_out.write(file_in.read())

    os.remove(source_file)
