import os


def move_file(command: str) -> None:
    args = command.split()

    if len(args) != 3 or args[0] != "mv" or args[1] == args[2]:
        return

    file_1 = args[1]
    file_2 = args[2]

    with open(file_1, "r") as from_file:
        data = from_file.read()

    full_path_file_list = file_2.split("/")
    file_name = full_path_file_list[-1]
    full_path_file_list.pop(-1)
    path_file = "/".join(full_path_file_list)

    if len(full_path_file_list) > 0:
        os.makedirs(path_file, exist_ok=True)
        file_name = path_file + "/" + file_name

    print(path_file, file_name)
    with open(file_name, "w") as to_file:
        to_file.write(data)

    os.remove(file_1)
