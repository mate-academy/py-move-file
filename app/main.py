import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    if parts[0] != "mv":
        return

    source_file = parts[1]
    destination_file = parts[2]

    if "/" not in destination_file:
        try:
            os.rename(source_file, destination_file)
        except FileNotFoundError:
            return
        return

    directory = "/".join(destination_file.split("/")[:-1])

    try:
        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(source_file, "r") as file_in:
            content = file_in.read()

        with open(destination_file, "w") as file_out:
            file_out.write(content)

        os.remove(source_file)

    except FileNotFoundError:
        return
