import os


class CommandError(Exception):
    pass


def move_file(command: str) -> None:
    command_split = command.split()

    if len(command_split) != 3 or command_split[0] != "mv":
        raise CommandError("invalid command")

    _, source, destination = command_split

    directory, file = os.path.split(destination)
    if not directory:
        os.rename(source, file)
    else:
        directory_path = os.path.dirname(destination)
        os.makedirs(directory_path, exist_ok=True)
        os.rename(source, destination)
