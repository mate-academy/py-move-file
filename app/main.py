import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) == 3:
        pass
    elif command_parts[0] == "mv":
        pass
    else:
        return

    src_path = command_parts[1]
    dst_parts = command_parts[2].split("/")
    dst_dirs = dst_parts[:-1]
    file_name = dst_parts[-1]
    new_dir = ""

    with open(src_path, "r") as file:
        content = file.read()

    if not dst_dirs:
        with open(file_name, "w") as new_file:
            new_file.write(content)

    else:
        for dirs in dst_dirs:
            new_dir = os.path.join(new_dir, dirs)

            if not os.path.exists(new_dir):
                os.mkdir(new_dir)

        with open(os.path.join(new_dir, file_name), "w") as new_file:
            new_file.write(content)

    os.remove(src_path)
