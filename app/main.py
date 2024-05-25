import os


def move_file(command: str) -> None:
    split_command = command.split()
    original_file_name = split_command[1]
    if "/" not in split_command[2]:
        with (open(original_file_name, "r") as original_file,
              open(split_command[2], "w") as renamed_file):
            renamed_file.write(original_file.read())
        os.remove(original_file_name)
    else:
        path_list = split_command[2].split("/")

        for directory in range(1, len(path_list)):
            if not os.path.exists("/".join(path_list[0:directory])):
                os.mkdir("/".join(path_list[0:directory]))

        with (open(original_file_name, "r") as original_file,
              open(split_command[2], "w") as moved_file):
            moved_file.write(original_file.read())
        os.remove(original_file_name)
