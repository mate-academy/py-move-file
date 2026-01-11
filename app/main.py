import os


def move_file(command: str) -> None:
    operation, filename, dir_file = command.split()
    dir_file_split = dir_file.split("/")
    if operation != "mv" or filename == dir_file:
        return
    file_path = ""
    for path in dir_file_split[:-1]:
        file_path = os.path.join(file_path, path)
    os.mkdir(file_path)
    with open(filename, "r") as source,\
            open(dir_file_split[-1], "w") as outcome:
        outcome.write(source.read())
        os.remove(filename)
