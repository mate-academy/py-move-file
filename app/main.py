import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        return
    code, old_file, new_file = command
    if "mv" == code:
        directory, file_name = os.path.split(new_file)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            for line in file_in:
                file_out.write(line)
        os.remove(old_file)
