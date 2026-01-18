import os


def move_file(command: str) -> None:
    cmd, file, new_file = command.split()
    if cmd != "mv":
        return

    directory = os.path.dirname(new_file)
    if not directory:
        os.rename(file, new_file)
    else:
        os.makedirs(directory)
        with (
            open(file, "r") as file_in,
            open(new_file, "w") as file_out
        ):
            file_out.write(file_in.read())
            os.remove(file)
