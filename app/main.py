import os


def move_file(command: str) -> None:
    parsed_command = command.split()
    path = parsed_command[-1].split("/")
    directory = ""

    for i in range(len(path) - 1):
        directory += path[i]
        if not os.path.exists(directory):
            os.mkdir(directory)
        directory += "/"
    directory += path[-1]

    with open(parsed_command[1], "r") as f:
        with open(directory, "w") as c:
            c.write(f.read())
        os.remove(parsed_command[1])
