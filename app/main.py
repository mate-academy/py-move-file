import os


class UnrecognizedException(BaseException):
    pass


def move_file(exec_string: str) -> None:
    commands = {"mv"}
    command, old_file, new_file = exec_string.split()
    if command not in commands:
        raise AttributeError(f"Allowed commands: {commands},"
                             f" {command} is not allowed!")
    path1, path2 = os.path.split(old_file)[0], os.path.split(new_file)[0]

    path1 = os.path.join(path1)
    path2 = os.path.join(path2)

    if path1 == path2:
        if old_file == new_file:
            return
        if old_file != new_file:
            if os.path.isfile(new_file):
                raise FileExistsError(f"{new_file} already exists, "
                                      f"process terminated.")
    try:
        os.renames(old_file, new_file)
    except BaseException as unknown:
        raise UnrecognizedException(f"All should be fine, but huge error "
                                    f"named {unknown} occurred.")
