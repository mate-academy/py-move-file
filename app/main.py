import os


def move_file(command: str) -> None:

    mv, old_file_name, new_path_file_name = command.split()

    path = os.path.dirname(new_path_file_name)

    new_file_name = new_path_file_name.split("/")[-1]

    if not new_file_name:
        new_file_name = old_file_name

    if path:
        os.makedirs(path, exist_ok=True)
        path += "/"

    with (open(old_file_name, "r") as old_file,
          open(path + new_file_name, "w") as new_file):
        new_file.write(old_file.read())

    os.remove(old_file_name)
