import os


class UnrecognizedException(BaseException):
    pass


def move_file(exec_string: str) -> None:
    commands = ["mv"]
    command, old_file, new_file = exec_string.split()
    if command != "mv":
        raise AttributeError(f"Allowed commands: {commands},"
                             f" {command} is not allowed!")
    path1, path2 = old_file.split("/")[:-1], new_file.split("/")[:-1]
    if path1 == path2:
        if old_file == new_file:
            return
        if old_file != new_file:
            if os.path.isfile(new_file):
                raise FileExistsError(f"{new_file} already exists, "
                                      f"process terminated")
    try:
        os.renames(old_file, new_file)
    except BaseException as unknown:
        raise UnrecognizedException(f"All should be fine, but huge error "
                                    f"named {unknown} occurred")
