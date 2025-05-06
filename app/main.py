import os


def move_file(command: str) -> None:

    split_command = command.split()

    if (len(split_command) == 3 and split_command[0] == "mv"
            and "/" in split_command[2]):
        _, old_file_name, future_path = split_command
        dir_path = os.path.dirname(future_path)
        os.makedirs(dir_path, exist_ok=True)

        with (open(old_file_name, "r") as old_file,
              open(future_path, "w+") as new_file):
            old_file_content = old_file.read()
            new_file.write(old_file_content)

        os.remove(old_file_name)

    if (len(split_command) == 3 and split_command[0] == "mv"
            and "/" not in split_command[2]):

        _, old_file_name, new_file_name = split_command

        with (open(old_file_name, "r") as old_file,
              open(new_file_name, "w+") as new_file):
            old_file_content = old_file.read()
            new_file.write(old_file_content)

        os.remove(old_file_name)
