import os


def move_file(command: str) -> None:
    arguments = command.split()
    if len(arguments[2].split("/")) > 1:
        directories = arguments[2].split("/")
        path = ""
        for directory in directories[:-1]:
            path += f"{directory}/"
            os.mkdir(path)
        with open(arguments[1], "r") as f:
            content = f.read()
            with open(f"{path}/{directories[-1]}", "w") as f:
                f.write(content)
        os.remove(arguments[1])
    else:
        os.rename(arguments[1], arguments[-1])
