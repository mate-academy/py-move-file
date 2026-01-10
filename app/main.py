import os


def move_file(command: str) -> None:
    command, file, path = command.split(" ")
    path_list = path.split("/")
    for i, directory in enumerate(path_list):
        if "." not in directory:
            if not os.path.exists(directory):
                os.makedirs("/".join(path_list[:i + 1]), exist_ok=True)
        else:
            with open(file, "r") as source, open(path, "w") as moved:
                moved.write(source.read())
            os.remove(file)
