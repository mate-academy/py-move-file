import os


class UnrecognizedException(BaseException):
    pass


def move_file(exec_string: str) -> None:
    commands = {"mv"}
    command, old_file, new_file = exec_string.split()
    if command not in commands:
        raise ValueError(f"Allowed commands: {commands},"
                         f" {command} is not allowed!")

    old_file, new_file = os.path.join(old_file), os.path.join(new_file)

    if old_file != new_file:
        if os.path.isfile(new_file):
            raise FileExistsError(f"{new_file} already exists, "
                                  f"process terminated.")
    try:
        os.renames(old_file, new_file)
    except BaseException as unknown:
        raise UnrecognizedException(f"All should be fine, but huge error "
                                    f"named {unknown} occurred.")
