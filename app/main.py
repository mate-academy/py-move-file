import os


def move_file(command: str) -> None:
    command_parts = command.split(" ")
    file_name = command_parts[1]
    new_file_path = command_parts[2]
    dir_list = command_parts[2].split("/")[:-1]
    if command_parts[0] != "mv":
        raise ValueError('There is not "mv" command')
    path = ""
    for elem in dir_list:
        path = os.path.join(path, elem)
        if not os.path.exists(path):
            os.mkdir(path)
    with (open(file_name, "r") as file_in,
          open(new_file_path, "w") as file_out):
        content = file_in.read()
        file_out.write(content)
    os.remove(file_name)