import os


def move_file(command: str) -> None:
    command_to_list = command.split(" ")
    start_file_name, destination_path = command_to_list[1], command_to_list[2]
    destination_path_list = destination_path.split("/")
    path = ""

    for folder_index in range(len(destination_path_list) - 1):
        path += destination_path_list[folder_index] + "/"
        try:
            os.mkdir(path)
        except FileExistsError:
            print("Folder already exists")

    if destination_path_list[-1] == "":
        os.rename(start_file_name,
                  destination_path + "new_" + start_file_name)
    else:
        os.rename(start_file_name, destination_path)
