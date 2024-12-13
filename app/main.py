from os import makedirs, remove, path


def move_file(command: str) -> None:
    separate_command = command.split()

    if separate_command[0] != "mv" and len(separate_command) != 3:
        return

    split_path = path.split(separate_command[2])
    if split_path[0]:
        makedirs(split_path[0], exist_ok=True)

    with (open(separate_command[1], "r") as file_in,
          open(separate_command[2], "w") as file_out):
        file_out.write(file_in.read())

    remove(separate_command[1])
