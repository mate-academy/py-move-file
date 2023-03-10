import os


def move_file(command: str) -> None:
    if command.split()[0] == "mv" and command.split() == 3:
        command, source_file_name, new_file_info = command.split()
        if "/" not in new_file_info:
            new_file_name = new_file_info
        else:
            directories, file_name = os.path.split(new_file_info)
            if directories:
                os.makedirs(directories, exist_ok=True)
            new_file_name = os.path.join(directories, file_name)
        with open(f"{source_file_name}", "r") as old_file:
            temp_text = old_file.read()
        os.remove(source_file_name)
        with open(f"{new_file_name}", "w") as new_file:
            new_file.write(temp_text)

