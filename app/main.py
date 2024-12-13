import os


class CommandError(Exception):
    pass


class ArgumentError(Exception):
    pass


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ArgumentError("Error in argument's string")
    command, filename, path_to_file = command.split()
    if command != "mv":
        raise CommandError("Wrong command")

    if os.path.exists(filename):
        path = os.path.dirname(path_to_file)
        if path:
            os.makedirs(path, exist_ok=True)

        os.replace(filename, path_to_file)
