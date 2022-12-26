import os


def move_file(command: str) -> None:
    command, old_file, new_file = command.split()
    if "mv" in command:
        directory = new_file.split("/")
        parent = ""
        if len(directory) > 1:
            for i in range(len(directory) - 1):
                parent = os.path.join(parent, directory[i])
                os.mkdir(parent)
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            for line in file_in:
                file_out.write(line)
            os.remove(old_file)
