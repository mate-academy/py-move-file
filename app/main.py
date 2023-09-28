import os
from typing import Any, Callable
from functools import wraps


class CommandError(Exception):
    """Checks command input for right format."""


def check_command(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(command: str) -> Any:
        if command.split()[0] != "mv" or len(command.split()) != 3:
            raise CommandError("Please enter valid command!")
        return func(command)

    return wrapper


@check_command
def move_file(command: str) -> None:
    _, source_name, target_name = command.split()
    if not os.path.dirname(target_name):
        os.rename(source_name, target_name)
    else:
        path_to_file = os.path.split(target_name)[0]
        os.makedirs(path_to_file, exist_ok=True)

        with (open(source_name, "r") as source,
              open(target_name, "w") as target):
            target.write(source.read())
        os.remove(source_name)
