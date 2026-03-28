import os


def move_file(command: str) -> bool:
    cmd, file1, file2 = command.split()
    if cmd != "mv" or file1 == file2:
        return False
    if "/" in file2:
        folders = os.path.dirname(file2)
        if not os.path.isdir(folders):
            os.makedirs(folders)
    with open(file1, "r") as file_in, open(file2, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(file1)
