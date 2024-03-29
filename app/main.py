import os


def move_file(command: str) -> None:
    _, start_file_name, destination_path = command.split(" ")
    destination_path_list = destination_path.split("/")
    if not len(destination_path_list) == 1:
        path = "/".join(destination_path_list[:len(destination_path_list) - 1])
        os.makedirs(path, exist_ok=True)

    if destination_path_list[-1] == "":
        os.rename(start_file_name,
                  destination_path + "new_" + start_file_name)
    else:
        os.rename(start_file_name, destination_path)
