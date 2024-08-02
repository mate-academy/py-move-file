import os


def move_file(command: str) -> None:
    command_key_word, file_in_name, dir_destination = command.split()
    if command_key_word != "mv" or file_in_name == dir_destination:
        return

    *directories, file_out_name = dir_destination.split("/")
    if not directories:
        os.rename(file_in_name, file_out_name)
        return

    parent_dir = ""
    for i in range(len(directories)):
        path = os.path.join(parent_dir, directories[i])
        parent_dir = str(path)
        try:
            os.mkdir(path)
        except OSError:
            pass

    with (open(file_in_name, "r") as file_in,
          open(dir_destination, "w") as file_out):
        content = file_in.read()
        file_out.write(content)

    os.remove(file_in_name)
