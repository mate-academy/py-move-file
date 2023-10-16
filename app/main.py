import os


def move_file(command: str) -> None:
    command = command.split()
    dirs = command[2].split("/")
    if not len(dirs) == 1:
        for i in range(1, len(dirs)):
            try:
                os.mkdir("/".join(dirs[:i]))
            except FileExistsError:
                pass

    with open(command[1]) as file_in, open(command[2], "a") as file_out:
        for row in file_in:
            file_out.write(row)

    os.remove(command[1])
