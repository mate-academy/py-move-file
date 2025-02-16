import os


def move_file(command: str) -> None:
    command_to_list = command.split()
    cmd, file_to_move, new_file = command_to_list
    origin_path = "D:/py-move-file/"
    if len(command_to_list) != 3:
        raise ValueError(f"Wrong number of arguments."
                         f" Got {len(command_to_list)} should 3")
    if cmd != "mv":
        raise ValueError(f"Invalid command {cmd}")
    if "/" not in new_file:
        os.renames(file_to_move, new_file)
    else:
        directory = new_file.split("/")
        new_file_path = origin_path
        for name_dir in directory:
            if ".txt" not in name_dir:
                new_file_path += f"{name_dir}/"
            os.makedirs(new_file_path, exist_ok=True)
        with (open(file_to_move, "r") as file_old,
              open(os.path.join(new_file_path, directory[-1]), "w")
              as file_new):
            file_new.write(file_old.read())
        os.remove(file_to_move)
