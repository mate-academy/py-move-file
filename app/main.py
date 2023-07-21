import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        cmd, file1, path_file2 = command.split()
        if cmd == "mv" and "/" in path_file2:
            path, file2 = os.path.split(path_file2)
            os.makedirs(path, exist_ok=True)
            with open(file1, "r") as file_in, open(path_file2, "w") as file_out:
                file_out.write(file_in.read())
            os.remove(file1)
        else:
            os.rename(file1, path_file2)
