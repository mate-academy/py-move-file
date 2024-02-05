import os


class CommandLenError(Exception):
    pass


class CommandNameError(Exception):
    pass


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3:
        raise CommandLenError("Command should have 3 arguments.")

    command, original_file, full_path = command_split
    if command != "mv":
        raise CommandNameError("Command must begin with 'mv'.")

    directory, file = os.path.split(full_path)
    if not directory:
        os.rename(original_file, file)
    else:
        directory_path = os.path.dirname(full_path)
        os.makedirs(directory_path, exist_ok=True)
        os.rename(original_file, full_path)
