import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) == 3 and parts[0] == "mv":
        old_file, full_path_to_new_file = parts[1:]
        dirs, new_file = os.path.split(full_path_to_new_file)

        if dirs:
            os.makedirs(dirs, exist_ok=True)

        with (
            open(old_file, "r") as file_in,
            open(full_path_to_new_file, "w") as file_out
        ):
            file_out.write(file_in.read())

        os.remove(old_file)
