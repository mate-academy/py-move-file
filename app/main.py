import os


def move_file(command: str) -> None:
    command_split_arr = command.split()
    if command_split_arr[0] != "mv":
        raise Exception(f"There is not '{command_split_arr[0]}' command!")
    if len(command_split_arr) != 3:
        raise Exception(f"Expected 3 arguments, got: {len(command_split_arr)}")
    try:
        os.makedirs(command_split_arr[2][:-1])
    except FileExistsError:
        pass
    with (
        open(command_split_arr[1], "r") as f_file,
        open(command_split_arr[2], "w") as s_file
    ):
        s_file.write(f_file.read())
        os.remove(command_split_arr[1])
