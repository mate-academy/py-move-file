import os


def move_file(command: str) -> None:
    cmd, source, target = command.split(" ")
    if target.endswith("/"):
        target += source
    folders = target.split("/")[:-1]
    path = ""
    for folder in folders:
        path += folder + "/"
        if not os.path.exists(path):
            os.mkdir(path)
    with open(source) as file_in, open(target, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(source)
