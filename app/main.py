import os


def move_file(command: str) -> None:
    command_attr = command.split()

    if len(command_attr) != 3 or command_attr[0] != "mv":
        return

    file_name = command_attr[1]
    if not os.path.exists(file_name):
        print("File not exist")
        return

    file_name_new = command_attr[2]

    if os.path.dirname(file_name) == os.path.dirname(file_name_new):
        if file_name != file_name_new:
            os.rename(file_name, file_name_new)
        return

    dir_path = os.path.dirname(file_name_new)

    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with (open(file_name, "r") as file_in,
          open(file_name_new, "w") as file_move):
        file_move.write(file_in.read())

    os.remove(file_name)
