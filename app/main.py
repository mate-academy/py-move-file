import os


def move_file(command: str) -> None:
    """this IF-block just will rename file without moving somewhere"""
    parts = command.split()

    if len(parts) == 3 and parts[0] == "mv":
        file_to_move, destination = parts[1], parts[2]
        destination_parts = destination.split("/")
        if len(destination_parts) == 1:
            os.rename(file_to_move, destination)
            return

        """this block just will open the existing dir"""
        *dirs, name_file_2_create = destination.split("/")
        if os.path.exists(f"{'/'.join(dirs)}"):
            with (
                open(file_to_move, "r") as moving_file,
                open(
                    f"{'/'.join(dirs)}/{name_file_2_create}", "w"
                ) as moved_file,
            ):
                moved_file.write(moving_file.read())
                os.remove(file_to_move)
                return

        """last possible way is to create dirs"""
        dir_path = ""
        for folder in dirs:
            dir_path += f"{folder}/"
            os.makedirs(dir_path, exist_ok=True)

        with open(file_to_move, "r") as moving_file, open(
            f"{dir_path}/{name_file_2_create}", "w"
        ) as moved_file:
            moved_file.write(moving_file.read())
            os.remove(file_to_move)
