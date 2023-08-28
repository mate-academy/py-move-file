import os


class InvalidCommandError(Exception):
    ...


def move_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3 or command_list[0] != "mv":
        raise InvalidCommandError("Unknown command.")

    _, origin_path, new_path = command_list

    dirs, _ = os.path.split(new_path)

    if dirs:
        os.makedirs(dirs, exist_ok=True)

    with (
        open(origin_path, "r") as source_file,
        open(new_path, "w") as new_file
    ):
        new_file.write(source_file.read())

    os.remove(origin_path)
