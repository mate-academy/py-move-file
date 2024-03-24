import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) == 3 and command[0] == "mv":
        directories, file_name = os.path.split(command[2])
        if directories:
            os.makedirs(directories, exist_ok=True)
            with (
                open(command[1], "r") as src_file,
                open(command[2], "w") as dst_file
            ):
                data = src_file.read()
                dst_file.write(data)
            os.remove(command[1])
        else:
            os.rename(command[1], command[2])
