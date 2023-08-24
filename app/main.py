import os


class InvalidCommandError(Exception):
    ...


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3 or command_list[0] != "mv":
        raise InvalidCommandError("Unknown command.")

    if "/" in command_list[2]:
        path = ""
        for folder in command_list[2].split("/")[:-1]:
            path = os.path.join(path, folder)
            if not os.path.isdir(path):
                os.mkdir(path)

    with (
        open(command_list[1], "r") as source_file,
        open(command_list[2], "w") as new_file
    ):
        new_file.write(source_file.read())

    os.remove(command_list[1])
