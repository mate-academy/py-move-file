import os


def move_file(command: str) -> None:
    args = command.split()

    if len(args) < 3:
        return

    cmd, path_in, path_out = args

    if cmd != "mv":
        return

    if path_in == path_out:
        return

    *dirs, file = path_out.split("/")

    for index in range(len(dirs)):
        try:
            os.mkdir("/".join(dirs[0:index + 1]))
        except FileExistsError:
            continue

    try:
        with open(path_in, "r") as file_in, open(path_out, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        print("File not found!")
        return

    os.remove(path_in)
