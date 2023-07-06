from os import makedirs, remove, path


def move_file(command: str) -> None:
    sep_command = command.split()

    if sep_command[0] != "mv":
        return

    split_path = path.split(sep_command[2])
    if split_path[0]:
        makedirs(split_path[0], exist_ok=True)

    with (open(sep_command[1], "r") as file_in,
          open(sep_command[2], "w") as file_out):
        file_out.write(file_in.read())

    remove(sep_command[1])
