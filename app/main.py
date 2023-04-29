import os


def move_file(command: str) -> None:
    command, old_file, new_file = command.split()
    if "mv" in command:
        directory = os.path.split(new_file)
        parent = ""
        if len(directory) > 1:
            for path in directory[:-1]:
                parent = os.path.join(parent, path)
                os.makedirs(parent)
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            for line in file_in:
                file_out.write(line)
            os.remove(old_file)
