import os


def move_file(command: str) -> None:
    if not command:
        return
    split_command = command.split()
    if len(split_command) != 3:
        return
    if split_command[0] != "mv":
        return

    file_name = split_command[1]
    dest_path = split_command[2]

    dir_name = os.path.dirname(dest_path)

    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    try:
        with open(file_name, "r") as file_in, \
                open(dest_path, "w") as file_out:
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        return

    os.remove(file_name)

