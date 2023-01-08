import os


def move_file(command: str) -> None:
    path_list = command.replace("/", " ").split(" ")
    path = ""

    for num_dir in range(2, len(path_list) - 1):

        path = os.path.join(path, path_list[num_dir])
        try:
            os.mkdir(path)
        except Exception:
            pass
    path = os.path.join(path, path_list[-1])

    with open(path_list[1], "r") as file_read, open(path, "w") as file_write:
        info_from_file = file_read.read()
        file_write.write(info_from_file)

    os.remove(path_list[1])
