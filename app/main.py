from shutil import move
from os import makedirs
from os.path import dirname, exists


class ArgumentException(Exception):
    pass


def move_file(command: str) -> None:
    try:
        cmd, source, destination = command.split()
        if cmd != "mv":
            raise ArgumentException("Unknown command")
        if not exists(source):
            raise FileNotFoundError(f"Unable to find the "
                                    f"source file at '{source}'")
    except ValueError:
        print("You have to provide 3 parameters in the command string")
    except ArgumentException as er:
        print(f"Invalid arguments: {er}")
    except FileNotFoundError as er:
        print(er)
    except Exception as er:
        print(f"Unexpected error: {er}")
    else:
        dest_dir = dirname(destination)
        if dest_dir:
            makedirs(dest_dir, exist_ok=True)
        move(source, destination)
