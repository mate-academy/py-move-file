import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source_file, destination_file = parts

    if source_file == destination_file:
        return

    try:
        if os.path.dirname(destination_file):
            os.makedirs(
                os.path.dirname(destination_file),
                exist_ok=True,
            )

        with open(source_file, "r") as file_in:
            content = file_in.read()

        with open(destination_file, "w") as file_out:
            file_out.write(content)

        os.remove(source_file)

    except FileNotFoundError:
        return
