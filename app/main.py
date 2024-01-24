from os import makedirs, path, remove, replace


class ErrorCommand(Exception):
    pass


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        mv, source_file, destination_file = command.split()
        destination_path = path.dirname(destination_file)
        if destination_path != "":
            makedirs(destination_path, exist_ok=True)
        if path.exists(destination_file):
            remove(destination_file)

        replace(source_file, destination_file)

    else:
        raise ErrorCommand("Wrong command. Command must include 3 arguments.")
