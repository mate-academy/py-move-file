from os import remove, rename, makedirs, path


def move_file(command: str) -> None:
    parts = command.split()
    if parts[0] != "mv" or len(parts) < 3:
        return

    if "/" not in parts[2]:
        rename(parts[1], parts[2])
        return

    file_to_copy_name, directory = parts[1], path.dirname(parts[2])

    if parts[2].endswith("/"):
        full_path = path.join(directory, path.basename(file_to_copy_name))
    else:
        full_path = path.join(directory, path.basename(parts[2]))

    if not path.exists(directory):
        makedirs(directory)

    with (
        open(file_to_copy_name) as file_to_read,
        open(full_path, "w") as file_to_write
    ):
        for line in file_to_read:
            file_to_write.write(line)

    remove(file_to_copy_name)
