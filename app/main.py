import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3 or command_list[0] != "mv":
        raise ValueError(
            "Invalid command format. Use: mv source_file destination_path"
        )

    origin_file = command_list[1]
    new_file_dir = command_list[2]

    if origin_file != new_file_dir:
        dir_path = os.path.dirname(new_file_dir)

        if dir_path:
            if os.path.exists(dir_path):
                if not os.path.isdir(dir_path):
                    raise FileExistsError(
                        f"'{dir_path}' exists but is not a directory."
                    )
            else:
                os.makedirs(dir_path)

        with open(origin_file, "r") as f1, open(new_file_dir, "w") as f2:
            f2.write(f1.read())
        os.remove(origin_file)
