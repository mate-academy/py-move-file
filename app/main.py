import os


def move_file(command: str) -> None:
    cmd, old_file_name, new_file_name = command.split()
    if cmd != "mv":
        return
    new_file_path = new_file_name.split("/")
    if len(new_file_name) > 1:
        current_dir = ""
        for dir_element in new_file_path[:-1]:
            try:
                os.mkdir(os.path.join(current_dir, dir_element))
            except FileExistsError:
                pass
            finally:
                current_dir = os.path.join(current_dir, dir_element)

    with (
        open(old_file_name, "r") as old_file,
        open(new_file_name, "w") as new_file
    ):
        new_file.write(old_file.read())
        os.remove(old_file_name)
