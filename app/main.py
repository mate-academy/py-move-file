import os


def move_file(command: str) -> None:
    first_split = command.split()
    if len(first_split) == 3:
        command = first_split[0]
        original_file = first_split[1]
        moving = first_split[2]
    else:
        return

    if (
        command == "mv"
        and os.path.exists(original_file)
    ):
        if os.path.sep in moving:
            path_parts = moving.split(os.path.sep)
            new_file = path_parts[-1]
            dir_path = os.path.sep.join(path_parts[:-1])
            if dir_path and not os.path.isdir(dir_path):
                os.makedirs(dir_path, exist_ok=True)
        else:
            new_file = moving

        if original_file == new_file:
            return

        with (
            open(original_file, "rb") as original,
            open(new_file, "wb") as new
        ):
            new.write(original.read())

        os.remove(original_file)
