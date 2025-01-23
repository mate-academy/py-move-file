import os


def move_file(command: str) -> None:
    (linux_command,
     old_file, new_file) = command.split(" ")
    if linux_command != "mv":
        raise ValueError(f"Invalid command: {linux_command}")
    if "/" in new_file:
        path_parts = new_file.split("/")
        new_file_path = os.path.join(*path_parts[:-1])
    else:
        os.rename(old_file, new_file)
        return

    if new_file_path and not os.path.exists(new_file_path):
        try:
            os.makedirs(new_file_path)
        except FileExistsError:
            pass

    with (open(old_file, "r") as old_file_obj,
          open(new_file, "w") as new_file_obj):
        new_file_obj.write(old_file_obj.read())

    os.remove(old_file_obj.name)
