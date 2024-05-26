from app.errors import WrongFormat


def validation_command(command_list: list) -> None:
    if len(command_list) != 3:
        raise WrongFormat(
            "There should be exactly three components:"
            " 'mv', a source file path, and a destination path.\n"
            "Expected format: 'mv \"<source>\" \"<destination>\"'"
        )

    if command_list[0] != "mv":
        raise WrongFormat(
            "The command should start with 'mv'."
        )
