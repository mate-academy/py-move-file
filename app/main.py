import os


def move_file(command: str) -> None:
    command_arr = command.split()

    os.makedirs(command_arr[2][:-1])
    with (
        open(command_arr[1], "r") as f_file,
        open(command_arr[2], "w") as s_file
    ):
        try:
            s_file.write(f_file.read())
        except FileExistsError:
            pass
        os.remove(command_arr[1])
