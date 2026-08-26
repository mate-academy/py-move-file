import os


class InvalidCommandFormatError(Exception):
    def __init__(self, command: str) -> None:
        message = (f"Command '{command}' must contain"
                   f" exactly 3 parts (got {len(command.split())})")
        super().__init__(message)


class NotMvCommandError(Exception):
    def __init__(self, cmd: str) -> None:
        message = f"Unsupported command '{cmd}', only 'mv' is allowed"
        super().__init__(message)


class SourceIsNotFileError(Exception):
    def __init__(self, source: str) -> None:
        message = f"'{source}' is not a file or does not exist"
        super().__init__(message)


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        raise InvalidCommandFormatError(command)

    cmd, source, path = command.split()

    if cmd != "mv":
        raise NotMvCommandError(cmd)

    if not os.path.isfile(source):
        raise SourceIsNotFileError(source)

    if "/" not in path:
        os.rename(source, path)
        return None

    if path.endswith("/"):
        path = os.path.join(path, os.path.basename(source))

    dir_path = os.path.dirname(path)

    os.makedirs(dir_path, exist_ok=True)
    with open(source, "r") as file_in, open(path, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(source)
