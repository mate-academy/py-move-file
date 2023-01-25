import os


def move_file(command: str) -> None:
    cmd, current_file_name, new_path = command.split()
    new_dirs, new_file_name = os.path.split(new_path)
    if len(new_dirs) > 1:
        os.makedirs(os.path.join(new_dirs), exist_ok=True)
    if len(new_dirs) == 1:
        os.rename(current_file_name, new_file_name)
    with open(current_file_name, "r") as source,\
            open(os.path.join(new_dirs, new_file_name), "w+") as new_path:
        new_path.write(source.read())
    os.remove(current_file_name)
