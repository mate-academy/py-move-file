import os


def move_file(command: str) -> None:
    input_command, file, new_file = command.split()

    if input_command == "mv":
        raise NameError(
            f"Command must be 'mv'. {input_command} is incorrect"
        )

    directory = os.path.dirname(new_file)

    if not directory:
        os.rename(file, new_file)
    else:
        os.makedirs(directory, exist_ok=True)

        with (
            open(file, "r") as file_read,
            open(new_file, "w") as file_write
        ):
            file_write.write(file_read.read())
            os.remove(file)
