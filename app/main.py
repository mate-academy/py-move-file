import os


def move_file(command: str) -> None:
    args = command.split()

    if len(args) != 3 or args[0] != "mv" or args[1] == args[2]:
        return

    source_pah = args[1]
    destination_path = args[2]

    with open(source_pah, "r") as from_file:
        data = from_file.read()

    full_path_file_list = destination_path.split("/")
    file_name = os.path.basename(destination_path)
    full_path_file_list.pop(-1)
    path_file = "/".join(full_path_file_list)

    if len(full_path_file_list) > 0:
        os.makedirs(path_file, exist_ok=True)
        file_name = os.path.join(path_file, file_name)

    with open(file_name, "w") as to_file:
        to_file.write(data)

    os.remove(source_pah)
