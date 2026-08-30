import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) != 3 or split_command[0] != "mv":
        return

    original_file_name = split_command[1]
    if len(original_file_name.split(".")) != 2 or "/" in original_file_name:
        return

    new_file_path = split_command[2]
    dir_name = os.path.dirname(new_file_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    with (open(original_file_name) as original_file,
          open(new_file_path, "w") as new_file):
        for line in original_file:
            new_file.write(line)

    os.remove(original_file_name)
