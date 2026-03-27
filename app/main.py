import os


def move_file(command: str) -> None:
    splitted = command.split()
    if len(splitted) != 3 or splitted[0] != "mv":
        raise ValueError("Wrong command")

    _, source_path, destination_path = splitted

    directories = os.path.dirname(destination_path)
    if directories:
        os.makedirs(directories, exist_ok=True)

    try:
        with (
            open(source_path, "r") as source_file,
            open(destination_path, "w") as destination_file
        ):
            for line in source_file:
                destination_file.write(line)

    except FileNotFoundError:
        return

    os.remove(source_path)
