import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    old_file_path = command_parts[1]
    new_file_path = command_parts[2]

    slash_last_index = new_file_path.rfind("/")

    if slash_last_index == -1:
        os.rename(old_file_path, new_file_path)
        return

    new_file_name = new_file_path[slash_last_index:]

    dirs_path = new_file_path[0:slash_last_index]

    cur_path = ""

    directories = dirs_path.split("/")

    for directory in directories:
        cur_path += (directory + "/")

        if not os.path.isdir(cur_path):
            os.mkdir(cur_path)

    with open(old_file_path, "r") as file:
        content = file.read()

    path_to_move = new_file_path if new_file_name else (new_file_path
                                                        + old_file_path)

    with open(path_to_move, "w") as new_file:
        new_file.write(content)

    os.remove(old_file_path)
