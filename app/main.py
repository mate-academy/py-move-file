import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "mv":
        raise Exception("Wrong command")

    path_to_file = command[2].split("/")
    path_to_file = "/".join(path_to_file[:-1])    # make path without file name
    if path_to_file == "":
        os.rename(command[1], command[2])
    else:
        os.makedirs(path_to_file, exist_ok=True)
        with (
            open(command[1], "r") as file_in,
            open(command[2], "w") as file_out
        ):
            file_out.write(file_in.read())
        os.remove(command[1])
