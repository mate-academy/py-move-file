from os import mkdir, remove


def move_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3 or command_list[0] != "mv":
        return

    _, source_file_name, dest_file_path = command_list

    dir_path = dest_file_path.split("/")[:-1]

    for i in range(len(dir_path)):
        try:
            mkdir("/".join(dir_path[:i + 1]))
        except FileExistsError:
            continue

    with open(source_file_name, "r") as source_file:
        content = source_file.read()

    with open(dest_file_path, "w") as dest_file:
        dest_file.write(content)
        remove(source_file_name)
