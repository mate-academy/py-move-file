import os


def move_file(command: str) -> None:
    command = command.split()

    if command[0] != "mv":
        raise ValueError("Command must be 'mv'")

    if "/" not in command[-1]:
        with (
            open(command[1], "r") as file_in,
            open(command[2], "w") as file_out
        ):
            file_out.write(file_in.read())
    else:
        folders, file = os.path.split(command[-1])
        os.makedirs(folders, exist_ok=True)
        with (
            open(command[1], "r") as file_in,
            open(command[-1], "w") as file_out
        ):
            file_out.write(file_in.read())
            os.remove(command[1])
