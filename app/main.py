import os


def move_file(command: str) -> None:
    command_elements = command.split()
    if len(command_elements) != 3 or command_elements[0] != "mv":
        raise ValueError('"command" must be a string with command "mv", '
                         "file name to move and new file name(path), "
                         "separated by spaces.")

    file_to_move_path, new_file_path = command_elements[1:]
    assert os.path.exists(file_to_move_path),\
        f"There is no file {file_to_move_path}"
    new_path = os.path.split(new_file_path)[0]
    if new_path and not os.path.exists(new_path):
        os.makedirs(new_path)

    with (open(file_to_move_path, "r") as f_to_read,
          open(new_file_path, "w") as f_to_write):
        f_to_write.write(f_to_read.read())
    os.remove(file_to_move_path)
