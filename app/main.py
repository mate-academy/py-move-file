from os import mkdir, remove, path


def move_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3 or command_list[0] != "mv":
        return

    _, source_file_name, dest_file_path = command_list

    if dest_file_path.endswith("/"):
        dest_file_path = path.join(dest_file_path,
                                   path.basename(source_file_name))

    dir_path = dest_file_path.split("/")[:-1]

    for i in range(len(dir_path)):
        try:
            dest_path = path.join(*dir_path[:i + 1])
            mkdir(dest_path)
        except FileExistsError:
            continue

    with open(source_file_name, "r") as source_file:
        content = source_file.read()

    with open(dest_file_path, "w") as dest_file:
        dest_file.write(content)
        remove(source_file_name)
