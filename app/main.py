import os


def move_file(command: str) -> None:
    if not command:
        return
    split_command = command.split()
    if len(split_command) != 3:
        return
    if split_command[0] != "mv":
        return
    if len(split_command[2].split("/")) == 1:
        with (open(split_command[1], "r") as file_src,
              open(split_command[2], "w") as file_dest):
            file_dest.write(file_src.read())
        os.remove(split_command[1])
        return
    dir_path = os.path.dirname(split_command[2])
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    with (open(split_command[1], "r") as file_src,
          open(split_command[2], "w") as file_dest):
        file_dest.write(file_src.read())
    os.remove(split_command[1])
