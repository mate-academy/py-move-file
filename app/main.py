import os


def move_file(command: str) -> None:
    command_data = command.split()
    original_file = command_data[1]
    file_path = command_data[2]

    if command_data[0] != "mv" or len(command_data) != 3:
        return

    if "/" in file_path:
        path = ""
        folders = file_path.split("/")

        for folder_name in range(len(folders) - 1):
            path += folders[folder_name] + "/"
        os.makedirs(path) if not os.path.exists(path) else None

    with (open(original_file, "r") as file_in,
          open(file_path, "w") as file_to_move):
        file_to_move.writelines(file_in.readlines())

    os.remove(original_file)
