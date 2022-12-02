from os import makedirs, remove, path


def move_file(command: str) -> None:
    command = command.split()
    if command[0] != "mv":
        return

    filename_in = command[1]
    dirs_with_namefile = path.split(command[-1])
    makedirs(dirs_with_namefile[0])

    with (
        open(filename_in, "r") as file_in,
        open(command[-1], "w") as file_out
    ):
        file_out.write(file_in.read())
        remove(filename_in)
