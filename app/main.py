import os


def move_file(command: str) -> None:
    try:
        mv, current_file, copied_file_path = command.split()
    except ValueError:
        raise ValueError("Command is incorrect")
    if mv != "mv" or os.path.exists(current_file) is False:
        raise ValueError("Command is incorrect")
    copied_file_info = copied_file_path.split("/")
    if len(copied_file_info) == 1:
        os.rename(current_file, copied_file_info[0])
    else:
        path = f"{copied_file_info[0]}"
        for index_of_folder in range(1, len(copied_file_info)):
            os.mkdir(path)
            path += f"/{copied_file_info[index_of_folder]}"
        with open(current_file, "r") as file_in, open(path, "w") as file_out:
            file_out.write(file_in.read())
        os.remove(current_file)
