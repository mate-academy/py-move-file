import os


def move_file(command: str) -> None:
    cmd, file, new_file = command.split()
    if cmd != "mv":
        return
    if "/" not in new_file:
        os.rename(file, new_file)
        return
    os.makedirs(os.path.dirname(new_file))
    with (
        open(file, "r") as file_in,
        open(new_file, "w") as file_out
    ):
        file_out.write(file_in.read())
        os.remove(file)
