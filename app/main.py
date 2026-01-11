import os


def move_file(command: str) -> None:
    parts = command.split()

    if (len(parts) == 3) and (parts[0] == "mv"):
        old_file, full_name_new_file = parts[1:]

        if "/" not in full_name_new_file:
            os.rename(old_file, full_name_new_file)
        else:
            path_to_new_file = os.path.split(full_name_new_file)[0]
            os.makedirs(path_to_new_file, exist_ok=True)

            with (open(old_file, "r") as file_in,
                  open(full_name_new_file, "w") as file_out):
                file_out.write(file_in.read())
            os.remove(old_file)
