import os


def move_file(command: str) -> None:
    command_parts = command.split(" ")
    if command_parts[0] != "mv" or len(command_parts) != 3:
        raise ValueError("Command is incorrect")
    file_name = command_parts[1]
    new_file_path = command_parts[2]
    dir_list = command_parts[2].split("/")[:-1]
    path = ""
    for directory in dir_list:
        path = os.path.join(path, directory)
        if not os.path.exists(path):
            os.mkdir(path)
    with (open(file_name, "r") as file_in,
          open(new_file_path, "w") as file_out):
        content = file_in.read()
        file_out.write(content)
    os.remove(file_name)
