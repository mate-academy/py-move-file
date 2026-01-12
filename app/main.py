from os import remove, rename, makedirs, path


def move_file(command: str) -> None:
    command_path = command.split()
    if len(command_path) != 3 or "mv" != command_path[0]:
        return
    if "/" not in command_path[2]:
        rename(command_path[1], command_path[2])
        return

    _, source_file, destination_file = command_path

    if destination_file.endswith("/"):
        file_name = path.basename(source_file)
        destination_file = path.join(destination_file, file_name)

    directory = path.dirname(destination_file)

    if directory:
        makedirs(directory, exist_ok=True)

    with (open(source_file, "rb") as file_in,
          open(destination_file, "wb") as file_out):
        file_out.write(file_in.read())
    remove(source_file)
