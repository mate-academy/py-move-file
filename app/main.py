from os import path, makedirs, rename


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3:
        raise ValueError("Invalid command format")

    user_command, user_file, new_user_file = command_list
    dir_path, file_name = path.split(new_user_file)

    if dir_path:
        makedirs(dir_path, exist_ok=True)

    full_new_user_file = path.join(dir_path, file_name)

    if path.exists(full_new_user_file):
        raise FileExistsError("The file already exists.")

    rename(user_file, full_new_user_file)
