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

    directories = f_name_out.split("/")
    count_of_directories = len(directories)
    if count_of_directories == 1:
        os.rename(f_name_in, f_name_out)
        return

    directory = ""
    for index, value in enumerate(directories):
        directory = os.path.join(directory, value)
        if index == (count_of_directories - 1):
            continue
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass

    with open(f_name_in, "r") as file_in, open(directory, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(f_name_in)
