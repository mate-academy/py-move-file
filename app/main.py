import os


class InvalidCommandFormat(Exception):
    pass


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) < 3 or parts[0] != "mv":
        raise InvalidCommandFormat(
            "Please provide a command like 'mv source_file destination_path'"
        )

    source_file = parts[1]
    destination = parts[2]

    if source_file == destination:
        return

    make_dirs, new_file_name = os.path.split(destination)

    if make_dirs == "":
        os.rename(source_file, new_file_name)
        return

    os.makedirs(make_dirs, exist_ok=True)

    with (
        open(source_file, "r") as old_file,
        open(destination, "w") as new_file
    ):
        content = old_file.read()
        new_file.write(content)

    os.remove(source_file)
