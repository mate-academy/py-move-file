import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3:
        return
    if command_list[0] != "mv":
        return
    file_name = command_list[1]
    destination = command_list[2]

    if "/" in destination:
        #  Full directory path is everything except the new filename
        dir_path = os.path.dirname(destination)
        #  Create full directory structure if it doesn't exist
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, True)

    to_save_name = destination

    with (open(file_name, "r") as file_to_move,
          open(to_save_name, "w") as file_to_save):
        file_to_save.write(file_to_move.read())
    os.remove(file_name)
