import os


class InvalidCommandError(Exception):
    ...


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3 or command_list[0] != "mv":
        raise InvalidCommandError("Unknown command.")

    dirs, _ = os.path.split(command_list[2])
    os.makedirs(dirs)

    with (
        open(command_list[1], "r") as source_file,
        open(command_list[2], "w") as new_file
    ):
        new_file.write(source_file.read())

    os.remove(command_list[1])
