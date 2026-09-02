import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) != 3 or split_command[0] != "mv":
        return

    original_file_name = split_command[1]
    if len(original_file_name.split(".")) != 2 or "/" in original_file_name:
        return

    new_file_path = split_command[2]
    if new_file_path.endswith("/"):
        new_file_path += original_file_name
    dir_path = os.path.dirname(new_file_path)
    if dir_path:
        formed_path = ""
        for folder in dir_path.split("/"):
            try:
                formed_path = os.path.join(formed_path, folder)
                os.mkdir(formed_path)
            except FileExistsError:
                continue

    with (open(original_file_name) as original_file,
          open(new_file_path, "w") as new_file):
        for line in original_file:
            new_file.write(line)

    os.remove(original_file_name)
