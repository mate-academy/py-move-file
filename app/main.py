import os


class CommandStringError(Exception):
    def __str__(self) -> str:
        return (
            "The command format must be: "
            "'mv [source file path] [destination file path].'"
        )


class OriginFileNotExistsError(Exception):
    def __init__(self, file_path: str = "") -> None:
        self.file_path = file_path

    def __str__(self) -> str:
        return f"Origin file {self.file_path} doesn't exist on server"


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise CommandStringError

    command_name, source, destination = command_parts

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    directory = os.path.dirname(destination)

    if directory:
        os.makedirs(directory, exist_ok=True)

    if not os.path.exists(source) or not os.path.isfile(source):
        raise OriginFileNotExistsError(source)

    with (open(source, "r") as file_source,
          open(destination, "w") as file_directory):
        file_directory.write(file_source.read())

    os.remove(source)
