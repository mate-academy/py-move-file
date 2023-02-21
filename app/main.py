import os


def move_file(command: str) -> None:
    path_in, path_out = command.split()[1:]

    if (index := path_out.rfind("/")) != -1:
        path_dirs = path_out[:index]
        os.makedirs(path_dirs, exist_ok=True)

    with open(path_in, "r") as file_in, open(path_out, "w") as file_out:
        for line in file_in:
            file_out.write(line)

    os.remove(path_in)
