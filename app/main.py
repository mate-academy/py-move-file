import os


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) == 3 or command_split[0] == "mv":
        command_name, filename, moved_file_path = command_split
        if "/" in moved_file_path:
            head, tail = os.path.split(moved_file_path)
            os.makedirs(head, exist_ok=True)
            with open(filename, "r") as file1,\
                    open(moved_file_path, "w") as file2:
                file2.write(file1.read())
            os.remove(filename)
        else:
            os.rename(filename, moved_file_path)
