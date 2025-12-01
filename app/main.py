import os


def move_file(command: str) -> None:
    parts = command.split()

    if parts[0] != "mv":
        return

    source = parts[1]
    destination = parts[2]

    dirs = parts[2].split("/")[0:-1]

    if dirs:
        dir_path = "/".join(dirs)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    with open(source, "r") as file1, open(destination, "w") as file2:
        content = file1.read()
        file2.write(content)

    os.remove(source)
