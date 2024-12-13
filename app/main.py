import os


def move_file(command: str) -> None:

    mv, old_file_name, new_path_file_name = command.split()

    path, new_file_name = os.path.split(new_path_file_name)

    if not new_file_name:
        new_file_name = old_file_name

    if path:
        os.makedirs(path, exist_ok=True)

    with (open(old_file_name, "r") as old_file,
          open(os.path.join(path, new_file_name), "w") as new_file):
        new_file.write(old_file.read())

    os.remove(old_file_name)
