import os


class WrongCommand(Exception):
    pass


class NoSourceFile(Exception):
    pass


def check_for_errors(command: str) -> None:
    if len(command.split()) != 3:
        raise WrongCommand(
            "Please enter command in this format: "
            "mv source_filename destination_filename"
        )

    command_name, filename, move_filename = command.split()

    if command_name != "mv":
        raise WrongCommand(
            "Command for moving file should be: mv"
        )

    if not os.path.exists(filename):
        raise NoSourceFile(f"Source file '{filename}' does not exist.")
