import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3:
        return
    if command_list[0] != "mv":
        return
    _, file_name, destination = command_list

    if "/" in destination:
        #  Full directory path is everything except the new filename
        dir_path = os.path.dirname(destination)
        #  Create full directory structure if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)

    to_save_name = destination
    if to_save_name[-1] == "/":
        to_save_name = os.path.join(to_save_name, file_name)

    with (open(file_name, "r") as file_to_move,
          open(to_save_name, "w") as file_to_save):
        file_to_save.write(file_to_move.read())
    os.remove(file_name)
