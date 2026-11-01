import os


def move_file(command: str) -> None:
    parts = command.split()
    our_new_file_path = parts[2]
    dir_path = os.path.dirname(our_new_file_path)
    file_name = os.path.basename(our_new_file_path)

    if not file_name or os.path.isdir(our_new_file_path):
        file_name = os.path.basename(parts[1])
        our_new_file_path = os.path.join(our_new_file_path, file_name)
        dir_path = os.path.dirname(our_new_file_path)  # recalculate

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with (open(parts[1], "r") as old_file,
          open(our_new_file_path, "w") as new_file):
        new_file.write(old_file.read())
    os.remove(parts[1])
