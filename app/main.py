import os


class InvalidCommandError(Exception):
    ...


def move_file(command: str) -> None:
    command_name, origin_path, new_path = command.split()

    if len(command.split()) != 3 or command_name != "mv":
        raise InvalidCommandError("Unknown command.")

    dirs, _ = os.path.split(new_path)

    if dirs:
        os.makedirs(dirs, exist_ok=True)

    with (
        open(origin_path, "r") as source_file,
        open(new_path, "w") as new_file
    ):
        new_file.write(source_file.read())

    os.remove(origin_path)
