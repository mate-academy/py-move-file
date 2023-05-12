import os


def move_file(command: str) -> None:
    com_spl = command.split()
    if len(com_spl) != 3:
        return
    cmd, file_old, path_file = com_spl
    if path_file.find("/") > -1 and os.path.exists(path_file) is False:
        new = os.path.dirname(path_file)
        os.makedirs(new, exist_ok=True)
        with (
            open(file_old, "r") as file_one,
            open(path_file, "w") as file_new
        ):
            file_new.write(file_one.read())
        os.remove(file_old)

    elif os.path.isfile(file_old) and path_file.find("/") < 0:
        os.rename(file_old, path_file)
