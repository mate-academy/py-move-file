import os


def move_file(command: str) -> None:
    command = command.split()

    if len(command) != 3 or command[0] != "mv":
        raise Exception("Wrong command")
    old_file = command[1]
    new_file = command[2]

    only_path = os.path.dirname(new_file)    # make path without file name
    if only_path == "":
        os.rename(old_file, new_file)
    else:
        os.makedirs(only_path, exist_ok=True)
        with (
            open(old_file, "r") as file_in,
            open(new_file, "w") as file_out
        ):
            file_out.write(file_in.read())
        os.remove(old_file)
