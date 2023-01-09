import os


def move_file(command: str) -> None:
    name_command, original_file, new_path_and_file = command.split()
    path_list = new_path_and_file.split("/")
    path = ""

    for num_dir in range(len(path_list) - 1):
        path = os.path.join(path, path_list[num_dir])
        os.makedirs(path)

    path = os.path.join(path, path_list[-1])

    with open(original_file, "r") as file_read, open(path, "w") as file_write:
        file_write.write(file_read.read())

    os.remove(original_file)
