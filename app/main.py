import os
from shutil import copyfile


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 and command_parts[0] != "mv":
        raise ValueError(
            "The command must be in the following format: "
            "'mv file.txt some_path/new_file.txt'"
        )

    old_file_name = command_parts[1]
    new_file_path = command_parts[2]
    new_file_path_parts = new_file_path.split("/")
    new_file_name = new_file_path_parts[-1]

    if len(new_file_path_parts) > 1:
        directories_path = ""

        for i in range(len(new_file_path_parts) - 1):
            directories_path \
                = os.path.join(directories_path, new_file_path_parts[i])

        try:
            os.makedirs(directories_path)
        except FileExistsError:
            print("File already exists")

        copyfile(old_file_name, os.path.join(directories_path, new_file_name))
        os.remove(old_file_name)
    else:
        os.rename(old_file_name, new_file_name)


move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")
