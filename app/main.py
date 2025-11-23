import os


def move_file(input_command: str) -> None:
    try:
        command, old_file_path, new_file_path = input_command.split(" ")
        if command != "mv":
            raise ValueError
    except ValueError:
        return

    directories, new_file_name = os.path.split(new_file_path)
    if directories != "":
        os.makedirs(directories, exist_ok=True)

    if not new_file_name:
        new_file_path = os.path.join(
            new_file_path,
            os.path.basename(old_file_path)
        )

    with (open(old_file_path, "r") as old_file,
          open(new_file_path, "w") as new_file):
        new_file.write(old_file.read())

    os.remove(old_file_path)
