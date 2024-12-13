import os


class InvalidCommandError(Exception):
    pass


class CommandFormatError(InvalidCommandError):
    pass


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3:
        raise CommandFormatError("Invalid command format")

    instruction, f_name_in, f_name_out = command_split
    if instruction != "mv" or f_name_in == f_name_out:
        raise InvalidCommandError("Invalid command or file(s) name")

    head, tail = os.path.split(f_name_out)
    if not head:
        os.rename(f_name_in, f_name_out)
        return

    try:
        os.makedirs(head)
    except FileExistsError:
        pass

    path = os.path.join(head, tail)
    with open(f_name_in, "r") as file_in, open(path, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(f_name_in)
