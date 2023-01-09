import os


def move_file(command: str) -> None:
    name_command, original_file, new_path_and_file = command.split()
    path_list = new_path_and_file.replace("/", " ").split("")
    path = ""

    for num_dir in range(len(path_list) - 1):
        path = os.path.join(path, path_list[num_dir])
        try:
            os.mkdir(path)
        except Exception:
            pass
    path = os.path.join(path, path_list[-1])

    with open(original_file, "r") as file_read, open(path, "w") as file_write:
        info_from_file = file_read.read()
        file_write.write(info_from_file)

    os.remove(original_file)
