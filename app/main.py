import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    file_command, old_file_name, new_file_path = parts
    if file_command != "mv":
        return
    if os.path.abspath(old_file_name) == os.path.abspath(new_file_path):
        return
    if new_file_path.endswith("/"):
        os.makedirs(new_file_path, exist_ok=True)
        new_file_path = (os.path.join
                         (new_file_path, os.path.basename(old_file_name)))

    else:
        file_path = os.path.dirname(new_file_path)
        if file_path:
            os.makedirs(file_path, exist_ok=True)

    with (open(old_file_name, "r") as old_file,
          open(new_file_path, "w") as new_file):
        new_file.write(old_file.read())
    os.remove(old_file_name)
